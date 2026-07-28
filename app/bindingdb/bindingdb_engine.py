import requests


class BindingDBEngine:

    def __init__(self):
        print("BindingDB Engine Loaded Successfully")


    def search_binding(self, drug_name):

        print(f"\nSearching BindingDB for {drug_name}...")

        url = (
            f"https://bindingdb.org/axis2/services/BDBService/getLigandsByName?name={drug_name}"
        )

        try:

            response = requests.get(url, timeout=10)

            if response.status_code == 200:

                return {
                    "status": "Found",
                    "response_size": len(response.text)
                }

        except Exception:

            pass

        return {
            "status": "Not Found",
            "response_size": 0
        }
