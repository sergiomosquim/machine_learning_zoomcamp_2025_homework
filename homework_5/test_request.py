import requests
url = "http://localhost:9696/predict"

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url=url, json=client)
pred = response.json()

print(pred)
if pred['subscription']:
    print("The client will likely get a subscription")
else:
    print("The client is unlikely to get a subscription")