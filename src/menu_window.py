# -*- encoding:utf-8 -*-
import os
import pygame
import src.const as CONST
from pygame.locals import *
import src.data_harvest as dh
import codecs
import sys

pygame.font.init()

_image_library = {}
class MenuWindow:
    def __init__(self):

        # coloca o background
        background = pygame.image.load("img/menu.jpg")

        game_font = pygame.font.Font('src/sounds/Blood Thirst.ttf', 40)
        
        screen = pygame.display.set_mode((CONST.DISPLAY_SIZE_X, CONST.DISPLAY_SIZE_Y), FULLSCREEN)
        done = False
        clock = pygame.time.Clock()
        name = ""



        # loop principal
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        dh.name = name
                        done = True
                    else:
                        letra = event.unicode
                        letra.encode('ISO-8859-1')
                        name += letra

           
            dead_text_surface = game_font.render('Put your name here ' + str(name), False,(200,10,10))
            screen.fill((0, 0, 0))
            screen.blit(background, (0,70))
            screen.blit(dead_text_surface,(CONST.DISPLAY_SIZE_X - 950,600))
            pygame.display.flip()
            clock.tick(60)

