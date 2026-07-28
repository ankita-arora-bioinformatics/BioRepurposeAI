import requests


class ClinicalTrialsEngine:

    def __init__(self):
        print("Clinical Trials Engine Loaded Successfully")

    def search_trials(self, drug_name):

        print(f"\nSearching Clinical Trials for {drug_name}...")

        url = (
            "https://clinicaltrials.gov/api/query/study_fields"
            f"?expr={drug_name}"
            "&fields=NCTId,BriefTitle,Phase,OverallStatus"
            "&min_rnk=1"
            "&max_rnk=5"
            "&fmt=json"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            studies = data["StudyFieldsResponse"]["StudyFields"]

            return studies

        return []
