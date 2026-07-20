import requests

target_id = input("Enter Target ChEMBL ID : ")

print("\nSearching Drug Candidates...\n")

url = f"https://www.ebi.ac.uk/chembl/api/data/activity.json?target_chembl_id={target_id}&limit=10"

response = requests.get(url, timeout=10)

print("Status Code :", response.status_code)

if response.status_code == 200:

    data = response.json()

    if data["activities"]:

        print("\nDrug Activities Found:\n")

        count = 1

        for activity in data["activities"]:

            print("=" * 60)
            print(f"Activity {count}")

            print("Molecule ChEMBL ID :",
                  activity.get("molecule_chembl_id", "N/A"))

            print("Assay ChEMBL ID :",
                  activity.get("assay_chembl_id", "N/A"))

            print("Activity Type :",
                  activity.get("standard_type", "N/A"))

            print("Activity Value :",
                  activity.get("standard_value", "N/A"))

            print("Units :",
                  activity.get("standard_units", "N/A"))

            count += 1

    else:

        print("No Drug Activities Found")

else:

    print("Connection Failed")
