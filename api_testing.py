import requests
import json

response  = requests.get("https://dummy-json.mock.beeceptor.com/continents")

response_json = json.loads(response.text)

for i in range(len(response_json)):
    countries = response_json[i]["developedCountries"]

    for contry in countries:
        if contry == "Egypt":
            print("Yes its present")
        else:
            print("No its not present")

for i in range(len(response_json)):
    oceans = response_json[i]["oceans"]

    for ocean in oceans:
        if ocean == "Indian Ocean":
            print("Yes its present")
        else:
            print("No its not present")
