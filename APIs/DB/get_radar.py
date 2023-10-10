import requests, sys
north = sys.argv[1]
south = sys.argv[2]
east = sys.argv[3]
west = sys.argv[4]
req = f'https://v5.db.transport.rest/radar?north={north}&west={west}&south={south}&east={east}'

response = requests.get(req)
print(response.text)