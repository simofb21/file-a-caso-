#include <Windows.h>
#include <stdio.h>

// Funzione per verificare se il file esiste
int fileExists(const wchar_t* filePath) {
    FILE* file = _wfopen(filePath, L"r");
    if (file) {
        fclose(file);
        return 1;
    }
    return 0;
}

int main() {
    // Percorso dell'immagine
    const wchar_t* imagePath = L"C:\\Users\\simof\\OneDrive\\Desktop\\garaCrema.jpg";

    // Verifica se il file esiste
    if (!fileExists(imagePath)) {
        wprintf(L"Il file specificato non esiste: %s\n", imagePath);
        return 1;
    }

    // Imposta l'immagine come sfondo desktop
    if (SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, (void*)imagePath, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)) {
        wprintf(L"Lo sfondo del desktop è stato cambiato con successo.\n");
    } else {
        wprintf(L"Errore nel cambiare lo sfondo del desktop. Codice errore: %lu\n", GetLastError());
    }

    return 0;
}