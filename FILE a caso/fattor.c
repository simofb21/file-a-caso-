#include <stdio.h>
#include <stdlib.h>

int fattoriale(int n) {
    int fat;
    if(n == 0 || n == 1) {
    return 1;
    }   
    else {
        return n * fattoriale(n - 1);
    }
}
int main() {
    int n;
    printf("Inserisci un numero: ");
    scanf("%d", &n);
    int fatt=fattoriale( n);
    printf("Il fattoriale di %d e' %d\n", n, fatt);
    return 0;
}