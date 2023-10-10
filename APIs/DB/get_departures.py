import requests, sys
#getting departures for bordeaux
stop = sys.argv[1]
departures = f'https://v5.db.transport.rest/stops/{stop}/departures?duration=120'

response = requests.get(departures)
print(response.text)