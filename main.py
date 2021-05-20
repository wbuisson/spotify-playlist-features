import requests
import base64
import json
from secrets import *

# Step 1 - Authorization 
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{CLIENT_ID}:{CLIENT_SECRET}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

# API call
r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']


endpoint_url = "https://api.spotify.com/v1/recommendations?"
query = f'{endpoint_url}limit=10&market=US&seed_artists=76B4kqqCUdVdAo9AG5LNWF%2c30FDJPN3RtwJZ20g5YGCRX%2c5C8KyBfvAz9PSaOd30eIow%2c3D4WFT29xe0sfSkXNvpmRG'

response =requests.get(query, 
            headers={"Content-Type":"application/json", 
                   "Authorization":"Bearer " + token})

json_res = response.json()
track_
for item in json_res['tracks']:
