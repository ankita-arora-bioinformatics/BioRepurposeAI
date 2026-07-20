import requests

protein = input("Enter Protein Name : ")

print("\nSearching ChEMBL...\n")

url = f"https://www.ebi.ac.uk/chembl/api/data/target/search?q={protein}&format=json"

response = requests.get(url, timeout=10)

print("Status Code :", response.status_code)

if response.status_code == 200:

    data = response.json()

    if data["targets"]:

        target = data["targets"][0]

        print("\nTarget Found\n")

        print("Target ChEMBL ID :", target["target_chembl_id"])

        print("Target Name :", target["pref_name"])

        print("Organism :", target["organism"])

        print("Target Type :", target["target_type"])

    else:

        print("No Target Found")

else:

    print("Connection Failed")
