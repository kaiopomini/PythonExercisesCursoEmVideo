import pygame
pygame.mixer.init()
pygame.base.init()
pygame.mixer.music.load('C:/system.mp3')
pygame.mixer.music.play()
pygame.event.wait()

'''
outra biblioteca que da pra usar é playsound, sendo o codigo o seguinte:

import playsound
playsound.playsound('C:/system.mp3')

'''