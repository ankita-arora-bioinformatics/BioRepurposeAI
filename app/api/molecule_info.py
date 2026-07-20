import requests

molecule = input("Enter Molecule ChEMBL ID : ")

print("\nGetting Molecule Information...\n")

url = f"https://www.ebi.ac.uk/chembl/api/data/molecule/{molecule}.json"

response = requests.get(url, timeout=10)

print("Status Code :", response.status_code)

if response.status_code == 200:

    data = response.json()

    print("\nMolecule Details\n")
    print("=" * 60)

    print("Molecule ChEMBL ID :", data.get("molecule_chembl_id", "N/A"))
    print("Preferred Name :", data.get("pref_name", "N/A"))
    print("Molecule Type :", data.get("molecule_type", "N/A"))
    print("Max Phase :", data.get("max_phase", "N/A"))

else:

    print("Connection Failed")
