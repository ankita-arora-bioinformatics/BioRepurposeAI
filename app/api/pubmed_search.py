import requests
import xml.etree.ElementTree as ET

gene = input("Enter Gene Name : ")

print("\nSearching PubMed...\n")

search_url = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    f"esearch.fcgi?db=pubmed&term={gene}&retmax=5"
)

response = requests.get(search_url, timeout=10)

root = ET.fromstring(response.text)

pmids = []

for id_tag in root.findall(".//Id"):
    pmids.append(id_tag.text)

if not pmids:
    print("No Papers Found")
    exit()

print("\nLatest Research Papers\n")

fetch_url = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    "efetch.fcgi?db=pubmed&id="
    + ",".join(pmids)
    + "&retmode=xml"
)

response = requests.get(fetch_url, timeout=10)

root = ET.fromstring(response.text)

for i, article in enumerate(root.findall(".//PubmedArticle"), start=1):

    print("=" * 60)
    print(f"Paper {i}")

    title = article.find(".//ArticleTitle")
    if title is not None:
        print("Title :", title.text)

    pmid = article.find(".//PMID")
    if pmid is not None:
        print("PMID :", pmid.text)

    year = article.find(".//PubDate/Year")
    if year is not None:
        print("Year :", year.text)
