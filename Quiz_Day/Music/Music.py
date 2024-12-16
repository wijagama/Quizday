import pygame
import sys

def reproducir_sonido(archivo_sonido):
    pygame.mixer.init()
    pygame.mixer.music.load(archivo_sonido)
    pygame.mixer.music.play()
    pygame.event.wait()  # Esperar hasta que termine la reproducción

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((400, 300))
    pygame.display.set_caption('Reproducir Sonido')

    sonido_path = "Win.wav"  # Reemplaza con la ruta a tu archivo de sonido WAV
    reproducir_sonido(sonido_path)

    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()
