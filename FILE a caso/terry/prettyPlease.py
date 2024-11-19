import requests

url = 'http://prettyplease.challs.olicyber.it/index.php'

# Parametri da inviare con la richiesta POST
data = {'how': 'pretty please'}

# Invia la richiesta POST
response = requests.post(url, data=data)

# Stampa la risposta
print(response.text)
