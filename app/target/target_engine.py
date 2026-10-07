import requests


class TargetEngine:

    def __init__(self):
        print("Target Resolver Loaded Successfully")


    def search_target(self, protein):

        print(f"\nSearching ChEMBL Target for {protein}...")

        # Temporary Target Mapping
        target_database = {

            "GADD34": {
                "chembl_id": "CHEMBL4630805",
                "target_name": "Protein Phosphatase 1 Regulatory Subunit 15A"
            },

            "AKT1": {
                "chembl_id": "CHEMBL2842",
                "target_name": "AKT Serine/Threonine Kinase 1"
            },

            "TP53": {
                "chembl_id": "CHEMBL3887",
                "target_name": "Tumor Protein P53"
            }

        }

        if protein in target_database:
            return target_database[protein]

        return {"error": "Target not found"}
