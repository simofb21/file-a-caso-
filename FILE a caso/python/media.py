def calcola_media(voti):
    if len(voti) == 0:
        return 0
    else:
        return sum(voti) / len(voti)

def main():
    num_voti = int(input("Quanti voti vuoi inserire? "))

    voti = []
    for i in range(num_voti):
        voto = float(input(f"Inserisci il voto {i + 1}: "))
        voti.append(voto)

    media = calcola_media(voti)
    print("La media dei voti è:", media)
 
if __name__ == "__main__":
    main()
