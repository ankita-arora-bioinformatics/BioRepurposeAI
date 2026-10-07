import requests


class ClinicalTrialsEngine:

    def __init__(self):
        print("Clinical Trials Engine Loaded Successfully")

    def search_trials(self, drug_name):

        print(f"\nSearching Clinical Trials for {drug_name} ...")

        url = "https://clinicaltrials.gov/api/v2/studies"

        params = {
            "query.term": drug_name,
            "pageSize": 5,
            "format": "json"
        }

        try:
            response = requests.get(url, params=params, timeout=20)

            if response.status_code != 200:
                print("ClinicalTrials.gov API Error:", response.status_code)
                return []

            data = response.json()

            studies = []

            for study in data.get("studies", []):

                protocol = study.get("protocolSection", {})

                identification = protocol.get(
                    "identificationModule", {}
                )

                status = protocol.get(
                    "statusModule", {}
                )

                design = protocol.get(
                    "designModule", {}
                )

                studies.append({
                    "NCTId": identification.get(
                        "nctId", "NA"
                    ),
                    "BriefTitle": identification.get(
                        "briefTitle", "NA"
                    ),
                    "Phase": design.get(
                        "phases", ["NA"]
                    ),
                    "OverallStatus": status.get(
                        "overallStatus", "NA"
                    )
                })

            return studies

        except Exception as e:
            print("Clinical Trials Error:", e)
            return []
