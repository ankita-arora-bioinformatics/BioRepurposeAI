import requests

gene_id = "23645"

url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id={gene_id}&retmode=json"

print("Getting Gene Information...")

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    info = data["result"][gene_id]

    print("\nOfficial Name :", info["name"])
    print("Description   :", info["description"])
    print("Organism      :", info["organism"]["scientificname"])
    print("Chromosome    :", info["chromosome"])

else:

    print("Connection Failed")
