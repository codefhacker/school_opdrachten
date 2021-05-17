# script_08_03_json_fietsenstalling
import json
import requests

stalling = requests.get("https://stallingsnet.nl/api/1/parkingcount/utrecht")
infoStalling = json.loads(stalling.text)
print(infoStalling)