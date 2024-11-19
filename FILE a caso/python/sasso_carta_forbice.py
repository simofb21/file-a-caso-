import random

def genera_scelta_ai():
    scelte_ai = ["sasso", "carta", "forbice"]
    return random.choice(scelte_ai)

def verifica_vittoria(scelta_giocatore, scelta_ai):
    if (
        (scelta_giocatore == "sasso" and scelta_ai == "forbice") or
        (scelta_giocatore == "carta" and scelta_ai == "sasso") or
        (scelta_giocatore == "forbice" and scelta_ai == "carta")
    ):
        return "giocatore"
    elif (
        (scelta_ai == "sasso" and scelta_giocatore == "forbice") or
        (scelta_ai == "carta" and scelta_giocatore == "sasso") or
        (scelta_ai == "forbice" and scelta_giocatore == "carta")
    ):
        return "ai"
    else:
        return "pareggio"

def gioca_partita():
    vittorie_giocatore = 0
    vittorie_ai = 0
    vittorie_consecutive_player = 0
    vittorie_consecutive_ai = 0

    nome_giocatore = input("Inserisci il tuo nome: ")

    print(f"Benvenuto, {nome_giocatore}! Il gioco terminerà quando uno dei due giocatori raggiungerà 11 punti, con due vittorie di fila, come nel pingpong oppure quando si avrà un massimo di 20 punti.\nIncominciamo!")

    while vittorie_giocatore <= 20 and vittorie_ai <= 20:
        # Scelte del giocatore e dell'AI
        scelte = ["sasso", "carta", "forbice"]
        scelta_giocatore = input("Scegli sasso, carta o forbice: ").lower()
        scelta_ai = genera_scelta_ai()

        # Stampa delle scelte
        print(f"{nome_giocatore.capitalize()}: {scelta_giocatore.capitalize()} | AI: {scelta_ai.capitalize()}")

        # Verifica delle regole e aggiornamento delle vittorie
        vincitore = verifica_vittoria(scelta_giocatore, scelta_ai)
        if vincitore == "giocatore":
            vittorie_giocatore += 1
            vittorie_consecutive_player += 1
            vittorie_consecutive_ai = 0
            print(f"{nome_giocatore.capitalize()} vince!\n")
        elif vincitore == "ai":
            vittorie_ai += 1
            vittorie_consecutive_player = 0
            vittorie_consecutive_ai += 1
            print("L'AI vince!\n")
        else:
            print("È un pareggio!\n")
            vittorie_consecutive_ai = 0
            vittorie_consecutive_player = 0

        # Stampa delle vittorie attuali
        print(f"Vittorie {nome_giocatore.capitalize()}: {vittorie_giocatore} | Vittorie AI: {vittorie_ai}\n")

        # Verifica delle vittorie consecutive
        if (vittorie_giocatore >= 20 or ((vittorie_ai<=9) and (vittorie_giocatore==11)) or ((vittorie_giocatore>=11 and vittorie_consecutive_player==2))):
            print(f"{nome_giocatore.capitalize()} ha vinto la partita!")
            break
        elif (vittorie_ai >= 20 or ((vittorie_giocatore<=9) and (vittorie_ai==11)) or ((vittorie_ai>=11 and vittorie_consecutive_ai==2))):
            print("L'AI ha vinto la partita!")
            break

# Avvia il gioco
gioca_partita()
