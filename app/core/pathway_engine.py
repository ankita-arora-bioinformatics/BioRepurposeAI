import requests
import re


class PathwayEngine:

    def __init__(self):
        print("Pathway Engine Loaded Successfully")

    def analyze_pathway(self, protein):

        print("\nStarting Pathway Analysis...")
        print("Protein :", protein)
        print("Searching Biological Pathways...")

        url = "https://reactome.org/ContentService/search/query"

        params = {
            "query": protein,
            "cluster": "true"
        }

        try:
            response = requests.get(
                url,
                params=params,
                timeout=15
            )

            if response.status_code != 200:
                print("Pathway Search Failed")

                return {
                    "protein": protein,
                    "pathways": [],
                    "count": 0,
                    "status": "Failed"
                }

            data = response.json()

            pathways = []

            # Reactome returns pathway results inside "results"
            # and actual records inside "entries"

            for group in data.get("results", []):

                for entry in group.get("entries", []):

                    if entry.get("type") == "Pathway":

                        name = entry.get("name", "")
                        st_id = entry.get("stId")

                        # Remove Reactome highlighting HTML
                        name = re.sub(
                            r"<[^>]+>",
                            "",
                            name
                        )

                        pathways.append({
                            "id": st_id,
                            "name": name
                        })

            print("\nPathways Found :", len(pathways))

            if len(pathways) > 0:

                print("\nTop Biological Pathways\n")

                for i, pathway in enumerate(
                    pathways[:5],
                    start=1
                ):

                    print(
                        str(i) + ".",
                        pathway["name"],
                        "| ID:",
                        pathway["id"]
                    )

            else:
                print("No Biological Pathways Found")

            return {
                "protein": protein,
                "pathways": pathways,
                "count": len(pathways),
                "status": "Success"
            }

        except Exception as e:

            print("Pathway Search Error :", e)

            return {
                "protein": protein,
                "pathways": [],
                "count": 0,
                "status": "Error"
            }
