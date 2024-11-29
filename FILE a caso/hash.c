#include <stdio.h>
#include <string.h>
#include <openssl/sha.h>

int nEl = 100



void sha256(const char str[], unsigned char output[SHA256_DIGEST_LENGTH]) {
    SHA256_CTX ctx;
    SHA256_Init(&ctx);
    SHA256_Update(&ctx, str, strlen(str));
    SHA256_Final(output, &ctx);
}

int main() {
    const char *stringa = "Esempio di stringa";
    unsigned char hash[SHA256_DIGEST_LENGTH];

    sha256(stringa, hash);

    // Stampa l'hash in formato esadecimale
    printf("SHA-256 di \"%s\": ", stringa);
    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++) {
        printf("%02x", hash[i]);
    }
    printf("\n");

    return 0;
}


int isValid(char hashata[] , char elenco[] []) {
    int valide = 0;
    for(int i = 0; i < nEl) {
        if(strcmp(hashata,elenco[i]) == 0)
            valide++;
    }
    if(valide > 0)
        return valide;
    else return -1
}
int main() {

}