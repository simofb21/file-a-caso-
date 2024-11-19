#include <SDL2/SDL.h>
#include <windows.h>

int main() {
    // ... (codice SDL come fornito)

    // Ottenere il path dell'immagine
    char imagePath[MAX_PATH];
    GetCurrentDirectory(MAX_PATH, imagePath);
    strcat(imagePath, "\\logo.png");

    // Impostare l'immagine come sfondo del desktop
    SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, imagePath, SPIF_UPDATEINIFILE);

    // Attendere che l'utente prema un tasto
    SDL_Event e;
    while (1) {
        if (SDL_PollEvent(&e) && e.type == SDL_QUIT)
            break;
    }

    // Libera le risorse
    SDL_FreeSurface(image);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
