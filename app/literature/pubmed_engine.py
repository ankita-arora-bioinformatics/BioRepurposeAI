import requests

import requests
class PubMedEngine:

    def __init__(self):
        print("PubMed Engine Loaded Successfully")

    def search_papers(self, gene):

        print(f"\nSearching PubMed for {gene}...")

        url = (
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
            f"esearch.fcgi?db=pubmed&term={gene}&retmode=json&retmax=5"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            papers = data["esearchresult"]["idlist"]

            return papers

        else:

            return []

    def get_paper_details(self, pubmed_id):

        url = (
            f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
            f"esummary.fcgi?db=pubmed&id={pubmed_id}&retmode=json"
        )

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            result = data["result"][str(pubmed_id)]

            return {
                "title": result.get("title", ""),
                "authors": result.get("authors", []),
                "journal": result.get("fulljournalname", ""),
                "pubdate": result.get("pubdate", "")
            }

        return {}
