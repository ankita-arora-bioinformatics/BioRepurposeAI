import requests


class DrugEngine:

    def __init__(self):
        print("Drug Engine Loaded Successfully")

    def search_drugs(self, chembl_id):

        print(f"\nSearching Drugs for {chembl_id} ...")

        url = (
            f"https://www.ebi.ac.uk/chembl/api/data/mechanism.json?"
            f"target_chembl_id={chembl_id}"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return data.get("mechanisms", [])

        return []
