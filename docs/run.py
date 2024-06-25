import requests

url = "http://localhost:4000/user-info/ylay/info"
 
response = requests.get(url)

if response.ok: 
	print(response.json())