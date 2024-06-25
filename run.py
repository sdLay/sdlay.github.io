import requests

baseurl = "https://sdlay.github.io/"
ext = "user-info/ylay/info.json"

url = baseurl + ext 
res = requests.get(url)

if res.ok:
	print(res.headers)
	print(res.json())
else:
	print("Failed to send GET request")