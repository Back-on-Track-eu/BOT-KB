import requests, sys
#location = sys.argv[1]
server = 'https://ressources.data.sncf.com/api/v2'                                               
cat = '/catalog/datasets'
response = requests.get(f'{server}{cat}')
print(response.text)