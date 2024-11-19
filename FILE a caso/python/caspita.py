ciphertext_hex = '104e137f425954137f74107f525511457f5468134d7f146c4c'
ciphertext_bytes = bytes.fromhex(ciphertext_hex)

# Prova tutti i possibili valori della chiave in un attacco a forza bruta
for key in range(256):
    # Ripeti la chiave sulla lunghezza del ciphertext
    repeated_key = bytes([key] * len(ciphertext_bytes))

    # Decifratura con XOR
    plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext_bytes, repeated_key)])

    # Stampa solo il tentativo con la chiave corrente
    print("Tentativo con chiave {}: {}".format(key, plaintext_bytes.hex()))

    # Verifica se il risultato sembra essere una flag
    if 'flag{' in plaintext_bytes.decode('utf-8', errors='replace') and '}' in plaintext_bytes.decode('utf-8', errors='replace'):
        print("Flag completa:", plaintext_bytes.hex())
        break
