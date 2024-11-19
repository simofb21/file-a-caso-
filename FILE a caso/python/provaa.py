import requests

response = requests.get('https://fb-bike.it/raceNews/partenzaTour.html')
print(response.text)         # Stampa il contenuto della risposta in formato testo
