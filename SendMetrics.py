# Sending metrics via DT API
import requests
url = '<https://<tenantid>.live.dynatrace.com/api/v2/metrics/ingest>'
payload = 'new_user_count,region=EAST count,delta=70'
h = {'Authorization' : 'Api-Token <token>'}
response = requests.post(url,payload,headers = h)
print(response.status_code)
