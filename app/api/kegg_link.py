import requests

gene_id = input("Enter KEGG Gene ID : ")

print("\nConnecting to KEGG...\n")

url = f"https://rest.kegg.jp/link/pathway/{gene_id}"

response = requests.get(url)

print("Status Code :", response.status_code)

if response.status_code == 200:

    if response.text:

        print("\nPathway Links:\n")
        print(response.text)

    else:

        print("No Pathway Found")

else:

    print("Connection Failed")
