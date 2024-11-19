import requests

url = "http://gabibbo-says.challs.olicyber.it/"
params = {'gabibbo': 'angry'}

response = requests.post(url, data=params)

print(response.text)
