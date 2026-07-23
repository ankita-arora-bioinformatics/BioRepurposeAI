import requests


class DrugDetailsEngine:

    def __init__(self):
        print("Drug Details Engine Loaded Successfully")

    def get_drug_details(self, molecule_id):

        print(f"\nFetching Drug Details for {molecule_id}...")

        url = (
            f"https://www.ebi.ac.uk/chembl/api/data/molecule/"
            f"{molecule_id}.json"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return {
                "name": data.get("pref_name", "NA"),
                "type": data.get("molecule_type", "NA"),
                "max_phase": data.get("max_phase", "NA"),
                "chembl_id": data.get("molecule_chembl_id", "NA")
            }

        return {
            "error": "Drug not found"
        }
