import requests

protein = input("Enter Protein Name : ")

print("\nSearching KEGG...\n")

url = f"https://rest.kegg.jp/find/genes/{protein}"

response = requests.get(url)

print("Status Code :", response.status_code)

if response.status_code == 200:

    if response.text:

        print("\nResults:\n")

        results = response.text.split("\n")

        print("\nHuman Results:\n")

        human_found = False

        for line in results:

            if line.startswith("hsa:"):

                print(line)
                human_found = True

        if not human_found:
            print("No Human Gene Found")

    else:

        print("No Result Found")

else:

    print("Connection Failed")
