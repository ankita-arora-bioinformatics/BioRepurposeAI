import requests


class DockingEngine:

    def __init__(self):
        print("Docking Engine Loaded Successfully")

    def prepare_docking(self, pdb_id, drug_name):

        print(f"\nPreparing Docking for {drug_name} with {pdb_id}...")

        pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"

        response = requests.get(pdb_url)

        if response.status_code == 200:

            return {
                "status": "Ready",
                "pdb_id": pdb_id,
                "drug": drug_name
            }

        return {
            "status": "Failed"
        }
