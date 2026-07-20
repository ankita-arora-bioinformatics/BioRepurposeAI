import requests

protein = input("Enter Protein Name : ")

print("\nSearching Drug Information...\n")

url = f"https://rest.uniprot.org/uniprotkb/search?query={protein}&format=json&size=1"

response = requests.get(url, timeout=10)

print("Status Code :", response.status_code)

if response.status_code == 200:

    data = response.json()

    if data["results"]:

        result = data["results"][0]

        print("\nProtein Found\n")

        print("UniProt ID :", result["primaryAccession"])

        print("Protein Name :")

        description = result.get("proteinDescription", {})

        if "recommendedName" in description:
            print(description["recommendedName"]["fullName"]["value"])

        elif "submissionNames" in description:
            print(description["submissionNames"][0]["fullName"]["value"])

        else:
            print("Protein name not available")

    else:

        print("Protein Not Found")

else:

    print("Connection Failed")
