#include <stdio.h>
#include <stdlib.h>
#include <string.h>

size_t base64_decode(const char *input, char *output) {
    const char *base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

    size_t input_len = strlen(input);
    size_t output_len = 0;

    for (size_t i = 0; i < input_len; i += 4) {
        char chunk[4];
        strncpy(chunk, input + i, 4);

        for (int j = 0; j < 4; j++) {
            if (chunk[j] == '=') {
                break;
            }

            chunk[j] = strchr(base64_chars, chunk[j]) - base64_chars;
        }

        output[output_len++] = (chunk[0] << 2) | (chunk[1] >> 4);
        output[output_len++] = (chunk[1] << 4) | (chunk[2] >> 2);
        output[output_len++] = (chunk[2] << 6) | chunk[3];
    }

    output[output_len] = '\0';
    return output_len;
}

int main() {
    // Parte 1: Decodifica dalla base64
    char parte1_base64[] = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE=";
    size_t parte1_len = strlen(parte1_base64);

    // Calcola la dimensione del buffer necessario per la decodifica
    size_t decode_size = ((parte1_len * 3) / 4) + 1;
    char parte1_decodificata[decode_size];

    // Decodifica dalla base64
    size_t decoded_len = base64_decode(parte1_base64, parte1_decodificata);

    // Parte 2: Converti il numero in bytes usando big endian
    unsigned long long parte2_numero = 664813035583918006462745898431981286737635929725;
    int num_bytes = sizeof(unsigned long long);
    char parte2_bytes[num_bytes];

    // Copia il numero nella rappresentazione di bytes usando big endian
    for (int i = num_bytes - 1; i >= 0; i--) {
        parte2_bytes[i] = (char)(parte2_numero & 0xFF);
        parte2_numero >>= 8;
    }

    // Unisci le due parti
    char flag_completa[decoded_len + num_bytes + 1];
    memcpy(flag_completa, parte1_decodificata, decoded_len);
    memcpy(flag_completa + decoded_len, parte2_bytes, num_bytes);
    flag_completa[decoded_len + num_bytes] = '\0';

    printf("Flag completa: %s\n", flag_completa);

    return 0;
}
