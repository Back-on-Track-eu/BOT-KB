import requests, sys
location = sys.argv[1]
locations = f'https://v5.db.transport.rest/stations?query={location}'

response = requests.get(locations)
print(response.text)