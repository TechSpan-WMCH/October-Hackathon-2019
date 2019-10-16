import requests
 
r = requests.get('http://httpbin.org/user-agent',
    headers = {'User-agent': 'TechSpan Security/2.0'})
print(r.headers['content-type'])
print(r.text)
data = r.json()
print(data)
print(data['user-agent'])

import requests
r = requests.get('http://techspan.org')
#print(r.headers)

#The below is merely a non-working PoC for what a server version scanner could look like. This could be quickly expedited by using a much faster method for banners in Python.
print("\n\nThe Apache server version is vulnerable:")
print(r.headers['Server'])
print("Refer to https://www.exploit-db.com/exploits/41570")
#print(r.text) return the html
