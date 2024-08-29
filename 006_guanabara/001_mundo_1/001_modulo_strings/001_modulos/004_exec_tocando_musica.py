#Faça um programa am Python qua abra a reproduza o áudio da um arquivo MP3.

import pygame
import time
#necessário iniciar a biblioteca
pygame.init()
#necessario adicionar o mixer:
pygame.mixer.music.load('004.001_exec_tocando_musica.mp3')
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play()
time.sleep(54)  

pygame.event.wait()



