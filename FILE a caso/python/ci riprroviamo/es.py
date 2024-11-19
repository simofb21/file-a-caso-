print("Benvenuto nel programma di verifica password")
print("Inserisci la tua password e ti dirò se è sicura o meno")
parola  = input("Parola: ")
print("Rinserisci la password che stiamo sereni e verifichiamo che è corretta ")

flag = 0

while flag !=1 : 
    parola2 = input("Parola: ")
    if parola == parola2:
        flag = 1
    else:
        print("Le password non coincidono, riprova")


if flag == 1: #quindi se la password è stata reinserita correttamente e basta
    if len(parola) < 8:
        print("La password è troppo corta")
    elif len(parola) > 16:
        print("La password è troppo lunga")
    else:
        print("La password è di lunghezza adeguata")
        if parola.isalnum():
            print("La password è composta solo da lettere e numeri")
        elif parola.isalpha():
            print("La password è composta solo da lettere")
        elif parola.isdigit():
            print("La password è composta solo da numeri")
        else:
            print("La password è composta da lettere, numeri e caratteri speciali")