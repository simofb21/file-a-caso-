#numero=int(input("Inserisci un numero: "))
#somma=0

#for i in range (0,numero+1):
 #   if i%2==0:
  #      somma+=i
#print(somma)

numero=int(input("Inserisci un numero: "))

for i in range (0, 11) : 
    print(f"{numero} * {i} = {numero * i}") 


    import re

def verifica_stringa(input_string):
    pattern = re.compile(r'^flag\{[^\d]{2}0[a-z][^\dL][L][\w]{4}[^a-pr-z]{3}[^\d]{2}\d[b]\}$')

    if pattern.match(input_string):
        print("La stringa corrisponde al pattern.")
    else:
        print("La stringa non corrisponde al pattern.")

# Esempi di utilizzo:
verifica_stringa("flag{ab0Lxyz_123b}")
verifica_stringa("questa_non_corrisponde")
