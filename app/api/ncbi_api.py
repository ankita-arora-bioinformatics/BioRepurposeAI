import requests

gene = "PPP1R15A"

url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term={gene}[Gene]+AND+Homo+sapiens[Organism]&retmode=json"

print("Searching NCBI...")

response = requests.get(url)

if response.status_code == 200:
    print("Connected Successfully!")
    data = response.json()

    print("\nNCBI Response:")
    print(data)
else:
    print("Connection Failed")
