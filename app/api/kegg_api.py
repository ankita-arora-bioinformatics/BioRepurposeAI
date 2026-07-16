import requests

print("Connecting to KEGG Server...")

url = "https://rest.kegg.jp/list/pathway/hsa"

response = requests.get(url)

print("Status Code :", response.status_code)

if response.status_code == 200:
    print("Connection Successful!")

    print("\nFirst Five Pathways:\n")

    pathways = response.text.split("\n")

    for pathway in pathways[:5]:
        print(pathway)

else:
    print("Connection Failed")
