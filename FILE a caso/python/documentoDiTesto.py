def compress_rle(input_string):
    compressed_string = ""
    count = 1

    # Itera attraverso la stringa
    for i in range(len(input_string) - 1):
        # Controlla se il carattere corrente è uguale al successivo
        if input_string[i] == input_string[i + 1]:
            count += 1
        else:
            # Se il carattere successivo è diverso, aggiungi il simbolo e il conteggio
            compressed_string += str(count) + input_string[i]
            count = 1

    # Aggiungi l'ultimo simbolo e il suo conteggio
    compressed_string += str(count) + input_string[-1]

    return compressed_string

# Esempio di utilizzo
input_string = "EAIOLKAAAASA"
compressed_result = compress_rle(input_string)

print(compressed_result)  # Output: "4A3B2C1D2A"
