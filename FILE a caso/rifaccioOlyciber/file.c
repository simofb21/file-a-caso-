#include <stdio.h>

int f(int x) {
    if (x <= 0) {
        return x;
    } else {
        return f(x - 1) - f(x - 2);
    }
}

int main() {
    int x = 20; // Esempio di chiamata alla funzione f con x = 5
    int result = f(x);
    printf("f(%d) = %d\n", x, result);
    return 0;
}
