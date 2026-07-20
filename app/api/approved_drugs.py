import requests

target = input("Enter Target ChEMBL ID : ")

print("\nSearching Approved Drugs...\n")

url = f"https://www.ebi.ac.uk/chembl/api/data/mechanism.json?target_chembl_id={target}"

response = requests.get(url, timeout=10)

print("Status Code :", response.status_code)

if response.status_code == 200:

    data = response.json()

    mechanisms = data.get("mechanisms", [])

    if mechanisms:

        print("\nApproved / Known Drugs\n")

        shown = set()

        for item in mechanisms:

            drug = item.get("molecule_chembl_id", "Unknown")

            action = item.get("mechanism_of_action", "Not Available")

            if drug not in shown:

                shown.add(drug)

                print("=" * 50)
                print("Drug ChEMBL ID :", drug)
                print("Mechanism :", action)

    else:

        print("No Drugs Found")

else:

    print("Connection Failed")
