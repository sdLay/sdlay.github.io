import requests

baseurl = "https://sdlay.github.io/"
ext = "user-info/ylay/info.json"
ext = ".well-known/webfinger?resource=acct:ylay@sdlay.github.io"

url = baseurl + ext 
res = requests.get(url)

if res.ok:
	print(res.headers)
	print(res.json())
else:
	print("Failed to send GET request")