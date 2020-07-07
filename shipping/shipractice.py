import requests
import shippo
import json
import pprint



shippo.config.api_key = 'shippo_live_8fb047d7a367ae99239fabe2ab91e74a705da4ef'

tracking = shippo.Track.get_status('ups', '1ZR0967V0317476280')

print(tracking)
#works but Shippo says I need to add billing, so this may not be free.

# track = requests.get('https://api.trackingmore.com/v2',headers=header)
#
# print(track.json())


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



# This works, not sure why python isn't
# curl https://api.goshippo.com/tracks/ups/1ZR0967V0317476280 \
#     -H "Authorization: ShippoToken shippo_live_8fb047d7a367ae99239fabe2ab91e74a705da4ef" \
#     -H "Content-Type: application/json"  \


#Python requests scrap:
# api_key = 'shippo_test_3d7ab3404e62fdee91aa2a6cce9b263c2479ec2d'
# header = {'Authorization': 'Bearer shippo_test_3d7ab3404e62fdee91aa2a6cce9b263c2479ec2d'}

# headers = {'Content-Type':'application/json',
#                'Authorization': 'shippo_live_8fb047d7a367ae99239fabe2ab91e74a705da4efd'}

# r = shippo.get('https://api.goshippo.com/tracks/ups/1ZR0967V0317476280')

# print(r.json())
