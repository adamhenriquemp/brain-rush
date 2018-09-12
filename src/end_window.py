# -*- encoding:utf-8 -*-
import os
import pygame
import src.const as CONST
from pygame.locals import *
import src.data_harvest as dh

_image_library = {}
class EndWindow:
    def __init__(self):

        # coloca o background
        background = pygame.image.load("img/background1.jpg")

        pygame.mixer.music.load('src/sounds/riso.mp3')
        pygame.mixer.music.play(0)

        game_font = pygame.font.Font('src/sounds/Blood Thirst.ttf', 60)
        dead_text_surface = game_font.render('You didnt make it', False,(255,0,0))

        game_font1 = pygame.font.SysFont('Comic Sans MS', 45)
        myscore_text_surface = game_font1.render('' + str(dh.name) + ' score: ' + str(dh.your_score[0]), False,(200,10,10))
        bestscore_text_surface = game_font1.render('Best score: ' + str(dh.best_score[0]), False,(200,10,10))
        
        screen = pygame.display.set_mode((CONST.DISPLAY_SIZE_X, CONST.DISPLAY_SIZE_Y), FULLSCREEN)
        done = False
        clock = pygame.time.Clock()

        # loop principal
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit(0)
           
            screen.fill((0, 0, 0))
            screen.blit(background, (0,70))
            screen.blit(dead_text_surface,(CONST.DISPLAY_SIZE_X - 730,30))
            screen.blit(myscore_text_surface,(CONST.DISPLAY_SIZE_X - 950,700))
            screen.blit(bestscore_text_surface,(CONST.DISPLAY_SIZE_X - 350,700))
            pygame.display.flip()
            clock.tick(60)


