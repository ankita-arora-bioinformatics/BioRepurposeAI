import requests


class PDBEngine:

    def __init__(self):
        print("PDB Engine Loaded Successfully")


    def search_pdb(self, protein_name):

        print(f"\nSearching PDB Structure for {protein_name}...")

        url = (
            "https://search.rcsb.org/rcsbsearch/v2/query"
        )

        query = {
            "query": {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_entity_source_organism.rcsb_gene_name.value",
                    "operator": "exact_match",
                    "value": protein_name
                }
            },
            "return_type": "entry",
            "request_options": {
                "paginate": {
                    "start": 0,
                    "rows": 5
                }
            }
        }

        response = requests.post(url, json=query)

        if response.status_code == 200:

            data = response.json()

            if "result_set" in data and len(data["result_set"]) > 0:

                return data["result_set"]

        return []
