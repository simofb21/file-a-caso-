def decrypt(text):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_text = ""
    
    for i in range(0, len(text), 5):
        group = text[i:i+5]
        if 'A' in group:
            decrypted_text += 'A'
        elif 'B' in group:
            decrypted_text += 'B'
        else:
            index = group.count('B')
            decrypted_text += alphabet[index]
    
    return decrypted_text

encrypted_text = "BBABA BABAB BBBBB BBAAB"
decrypted_text = decrypt(encrypted_text)
print("Decrypted text:", decrypted_text)
