# Programa em python que abre e reproduz um arquivo de áudio MP3
import pygame 
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
