import socket
import time

# Funzione per decifrare il segreto
def decifra_segreto(segreto, permutazione):
    segreto_decifrato = [0]*8
    for i in range(8):
        for j in range(256):
            if (j & permutazione[i]) == segreto[i]:
                segreto_decifrato[i] = j
                break
    return bytes(segreti_decifrati)

def main():
    host = "segreto.challs.olicyber.it"
    port = 33000

    # Connessione al servizio remoto
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Attesa del prompt iniziale
    print(s.recv(1024).decode())

    # Funzione per inviare una query e ottenere la risposta
    def invia_query(query):
        s.sendall(query.encode())
        return s.recv(1024).hex()

    # Funzione per inviare la risposta
    def invia_risposta(risposta):
        s.sendall(risposta.encode() + b"\n")

    # Loop per 10 round
    for i in range(10):
        print(f"Round {i+1} di 10")
        # Ottieni la permutazione
        permutazione = [int(invia_query(str(j))) for j in range(256)]
        # Decifra il segreto
        segreto_decifrato = decifra_segreto(b'', permutazione)
        # Invia la risposta
        invia_risposta(segreti_decifrati.hex())
        
        # Attesa della risposta del server
        response = s.recv(1024).decode()
        print(response)

    # Ricevi la flag
    flag = s.recv(1024).decode()
    print(flag)

    # Chiudi la connessione
    s.close()

if __name__ == "__main__":
    main()
