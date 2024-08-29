import requests

query_params = {"offset":2, "limit":2, "max_price":40}

response = requests.get(
    "https://apipheny.io/",
    params=query_params,
    )

print(response.json())