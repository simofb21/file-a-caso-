import requests

url = "http://web-02.challs.olicyber.it/server-records"
params = {"id": "flag"}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Flag:", response.text)
else:
    print("Errore:", response.status_code, response.text)
