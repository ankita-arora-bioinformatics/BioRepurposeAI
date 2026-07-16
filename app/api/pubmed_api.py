import requests

disease = "NAFLD"

url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={disease}&retmode=json&retmax=5"

print("Searching PubMed...\n")

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    result = data["esearchresult"]

    print("Total Papers :", result["count"])

    print("\nLatest Paper IDs:")

    for paper in result["idlist"]:
        print(paper)

else:

    print("Connection Failed")

