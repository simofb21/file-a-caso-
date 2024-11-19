def decrypt_caesar_cipher(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            # Determina se il carattere è maiuscolo o minuscolo
            if char.isupper():
                start = ord('A')
            elif char.islower():
                start = ord('a')
            else:
                # Se il carattere non è una lettera, aggiungilo direttamente al testo in chiaro
                plaintext += char
                continue

            # Decifra il carattere
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += decrypted_char
        else:
            # Se il carattere non è una lettera, aggiungilo direttamente al testo in chiaro
            plaintext += char
    return plaintext

# Stringa da decifrare
ciphertext = "synt{CAESAR_ME!-l0h_T07_vG_e1tuG!}"

# Prova a decifrare con diversi shift
for shift in range(1, 26):
    decrypted_text = decrypt_caesar_cipher(ciphertext, shift)
    print(f"Shift {shift}: {decrypted_text}")
