#check a gamer profile score list using Python
import requests
response = requests.get('http://services.runescape.com/m=hiscore/compare?user1=Zezima')
print (response.status_code)
print (response.content)
