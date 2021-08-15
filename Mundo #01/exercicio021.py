# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import os

# Inicializando o PyGame
pygame.init()

# Carregando o arquivo MP3 e executando
if os.path.exists('mp3/sadnarutin.mp3'):
    pygame.mixer.music.load('mp3/sadnarutin.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)

    clock = pygame.time.Clock()
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
else:
    print('O arquivo de som não está no diretório!!')
