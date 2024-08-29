import requests

try:
    response = requests.get("https://apipheny.io/")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(err)
else:
    print(response.status_code)
