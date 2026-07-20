import requests

pathway = input("Enter Pathway ID : ")

print("\nGetting Pathway Information...\n")

url = f"https://rest.kegg.jp/get/{pathway}"

try:
    response = requests.get(url, timeout=10)

except requests.exceptions.RequestException:

    print("Unable to connect to KEGG Server")

    exit()

print("Status Code :", response.status_code)

if response.status_code == 200:

    lines = response.text.split("\n")

    for line in lines:

        if line.startswith("NAME"):

            print("\nPathway Name:")

            print(line.replace("NAME", "").strip())
           
            break

else:

    print("Connection Failed")
