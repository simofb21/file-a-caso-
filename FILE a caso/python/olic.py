from Crypto.Util.number import inverse

data = bytes.fromhex("7f1d26c428628a1dd436311d36b0054536f1a79c62f1f59c7b4a8ffc9ca7f19c31bbf16b1dc062e6b2")

# Calcolare k in base ai dati cifrati
k = inverse(data[2] - 1, 256)

# Definire una funzione per decifrare un singolo byte
def dec(x):
    return ((x - 1) * k) % 256

# Applicare la funzione di decifratura a ogni byte dei dati cifrati
flag = bytes(map(dec, data))
print(flag)
