import requests

response = requests.get('https://https://posijar.com') #fa una richiesta get alla pagina web lincata lì
print(response.text)         # stampa il sorgente della pagina web