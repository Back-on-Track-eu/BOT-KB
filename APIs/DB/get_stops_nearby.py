import requests, sys
lat = sys.argv[1]
lon = sys.argv[2]
req = f'https://v5.db.transport.rest/stops/nearby?latitude={lat}&longitude={lon}'

response = requests.get(req)
print(response.text)