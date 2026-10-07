import requests


class DrugEngine:

    def __init__(self):
        print("Drug Engine Loaded Successfully")

    def search_drugs(self, chembl_id):

        print(f"\nSearching Drug Candidates for {chembl_id} ...")

        url = (
            "https://www.ebi.ac.uk/chembl/api/data/activity.json?"
            f"target_chembl_id={chembl_id}"
            "&limit=20"
        )

        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            return []

        data = response.json()
        activities = data.get("activities", [])

        candidates = []
        seen = set()

        for activity in activities:

            molecule_id = activity.get("molecule_chembl_id")

            if not molecule_id:
                continue

            if molecule_id in seen:
                continue

            seen.add(molecule_id)

            standard_type = activity.get("standard_type")
            standard_value = activity.get("standard_value")
            standard_units = activity.get("standard_units")

            # Fetch molecule information
            molecule_url = (
                f"https://www.ebi.ac.uk/chembl/api/data/molecule/"
                f"{molecule_id}.json"
            )

            molecule_response = requests.get(
                molecule_url,
                timeout=15
            )

            molecule_data = {}

            if molecule_response.status_code == 200:
                molecule_data = molecule_response.json()

            name = (
                molecule_data.get("pref_name")
                or molecule_id
            )

            molecule_type = (
                molecule_data.get("molecule_type")
                or "Unknown"
            )

            max_phase = molecule_data.get("max_phase")

            candidates.append({
                "molecule_chembl_id": molecule_id,
                "name": name,
                "molecule_type": molecule_type,
                "max_phase": max_phase,
                "standard_type": standard_type,
                "standard_value": standard_value,
                "standard_units": standard_units,
                "action_type": activity.get("action_type")
            })

        # Rank candidates
        def potency_value(candidate):

            value = candidate.get("standard_value")

            try:
                return float(value)
            except (TypeError, ValueError):
                return float("inf")

        candidates.sort(key=potency_value)

        print("\nTop Drug Candidates:")

        for i, candidate in enumerate(candidates[:5], start=1):
            print(
                f"{i}. {candidate['name']} "
                f"| ID: {candidate['molecule_chembl_id']} "
                f"| {candidate['standard_type']}: "
                f"{candidate['standard_value']} {candidate['standard_units']}"
            )

        return candidates
