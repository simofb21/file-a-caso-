import requests

url = "http://web-03.challs.olicyber.it/flag"
headers = {"X-Password": "admin"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Flag:", response.text)
else:
    print("Errore:", response.status_code, response.text)
