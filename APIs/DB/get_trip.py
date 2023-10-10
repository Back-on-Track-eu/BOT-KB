import requests, sys, urllib

tripid =  urllib.parse.quote(sys.argv[1])
lineName = sys.argv[2]
req = f'https://v5.db.transport.rest/trips/{tripid}?lineName={lineName}' 
print(req)
response = requests.get(req)
print(response.text)