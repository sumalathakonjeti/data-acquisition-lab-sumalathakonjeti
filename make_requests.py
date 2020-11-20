import urllib.request as request
import requests,json

limit = 1000
offset = 1
for i in range(40):
  url = "https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?limit=1000&offset"+str(offset)

  params = {
    'offset':offset,
    'limit':limit
  }

  headers = {
    'Content-Type': 'application/json',
    'token': 'HCzjGfPFPOmgmuVhWIShKinezlgcyMxg'
  }

  response = requests.request( 'GET',url, headers=headers, params = params)
  j = json.loads(response.text)
  with open('Location_'+str(i)+'.json', 'w') as f:
     json.dump(j, f, indent=4)

  offset += limit






