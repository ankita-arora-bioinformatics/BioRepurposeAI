import requests

print("Connecting to Internet...")

response = requests.get("https://www.google.com")

print("\nStatus Code:", response.status_code)

if response.status_code == 200:
    print("\nInternet Connection Successful!")
else:
    print("\nConnection Failed!")
