import requests, sys
location = sys.argv[1]
req = f'https://v5.db.transport.rest/locations?query={location}'
print(req)
response = requests.get(req)
print(response.text)