import requests
from_station = '8000001'
to_station = '8010085'
req = f'https://v5.db.transport.rest/journeys?from={from_station}&to={to_station}&bus=false&tickets=true'

response = requests.get(req)
print(response.text)