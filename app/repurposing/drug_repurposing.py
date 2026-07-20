import requests


class DrugRepurposingEngine:

    def __init__(self):
        print("Drug Repurposing Engine Loaded Successfully")


    def search_drugs(self, protein):

        print("\nSearching Drug Candidates...\n")

        url = (
            f"https://www.ebi.ac.uk/chembl/api/data/"
            f"target/search.json?q={protein}"
        )

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            data = response.json()

            if data["targets"]:

                target = data["targets"][0]

                print("=" * 60)
                print("Target Found")
                print("=" * 60)

                print("Target ChEMBL ID :", target["target_chembl_id"])
                print("Target Name      :", target["pref_name"])
                print("Organism         :", target["organism"])
                print("Target Type      :", target["target_type"])

            else:

                print("No Drug Target Found")

        else:

            print("Connection Failed")
