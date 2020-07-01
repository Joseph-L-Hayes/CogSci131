import requests
import shippo
import json
import pprint


shippo.config.api_key = 'shippo_test_3d7ab3404e62fdee91aa2a6cce9b263c2479ec2d'

r = requests.get('https://api.goshippo.com/tracks/usps/9205590164917312751089')

print(r.json())




# parameters = {"lat": 40.71, "lon": -74} #ISS coords for NYC
#
# response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
# people = requests.get("http://api.open-notify.org/astros.json")
#
# astros = people.json()
# # print(response.status_code)
# data = response.json()
#
# pprint.pprint(data)
# pprint.pprint(astros)
