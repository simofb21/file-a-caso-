import requests

# URL della risorsa per ottenere il cookie di sessione
login_url = "http://web-06.challs.olicyber.it/token"

# URL della risorsa per ottenere la flag
flag_url = "http://web-06.challs.olicyber.it/flag"

# Creazione di un oggetto Session
session = requests.Session()

# Esecuzione della richiesta GET per ottenere il cookie di sessione
response = session.get(login_url)

# Verifica della risposta per assicurarsi che la richiesta sia andata a buon fine
if response.status_code == 200:
    print("Cookie di sessione ottenuto con successo.")
    
    # Esecuzione di una richiesta GET alla risorsa della flag utilizzando lo stesso oggetto Session
    response_flag = session.get(flag_url)
    
    # Verifica della risposta per ottenere la flag
    if response_flag.status_code == 200:
        print("Flag:", response_flag.text)
    else:
        print("Errore durante il recupero della flag:", response_flag.status_code)
else:
    print("Errore durante il recupero del cookie di sessione:", response.status_code)
