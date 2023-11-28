import pygame.mixer
import time

def reproducir_mp3(ruta):
    pygame.mixer.init()
    pygame.mixer.music.load(ruta)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(1)
        
sonidoR2D2 = "/home/elliot/Downloads/r2d2.mp3"
#archivo_mp3 = "/"

reproducir_mp3(sonidoR2D2)