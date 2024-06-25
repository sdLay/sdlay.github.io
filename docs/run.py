import requests

url = "http://localhost:4000/user-info/ylay/info"
url = "https://daniellay.cc/.well-known/webfinger?resource=acct:dlay@daniellay.cc"

# url = "https://daniellay.cc/u/dlay/followers"
url = "https://daniellay.cc/u/dlay#key"
url = "https://daniellay.cc/u/dlay"
headers = {
	'accept': 'application/activity+json'
}

response = requests.get(url, headers=headers)

if response.ok: 
	# print(response.headrs)
	print(response.json())
else: 
	print(response.status_code)