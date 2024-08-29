import requests

response = requests.get("https://apipheny.io/")

print(response.status_code)

if response.status_code == 200:
    print("Success!")

elif response.status_code == 500:
    print("Server error.")

elif response.status_code == 404:
    print("Page not found.")