#Fetch RuneScape item data and print out a beautiful JSON dump.
import json
import requests
response = requests.get("http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item=556")
rsdata = json.loads(response.text)
print(json.dumps(rsdata, indent=4, sort_keys=True))
