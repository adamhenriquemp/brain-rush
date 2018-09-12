# -*- encoding:utf-8 -*-
import os
import pygame
import random
import datetime
import pandas as pd
from src.position import Position
from src.hero import Zombie
from src.ball import Ball
import src.const as CONST
import time
from pygame.locals import *
import src.data_harvest as data_harvest


_image_library = {}
#score = 0

class GameWindow:
    def __init__(self):
        
        pygame.font.init()
        #pygame.mixer.init()

        background = pygame.image.load("img/background2.jpg")

        game_font = pygame.font.SysFont('Comic Sans MS', 45)
        placar_font = pygame.font.SysFont('Comic Sans MS', 20)

        score = 0
        score_text_surface = game_font.render('Pontos: '+str(score), False,(255,255,255))
        arq = open('src/placar.txt', 'r')
        placar = int(arq.read())

        arq1 = open('src/nomeBest.txt', 'r')
        name = arq1.read()


        placar_text_surface = placar_font.render('Best Score: ' + name + ' - '+str(placar), False, (0,0,255))      

        def get_image(path):
            global _image_library
            image = _image_library.get(path)
            if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
            return image

        # variaveis do heroi
        hero = Zombie()
        hero_group = pygame.sprite.Group(hero)

        # variaveis da bolinha
        ball = Ball()
        ball.set_random_position(hero)

        #Timer Novo (bug do mouse)
        start_ticks = pygame.time.get_ticks()
        time_left = CONST.GAME_TIME

        mirror = False
        bug = False
        alreadySaid = [False, False, False, False, False, False] 
        opc0 = opc1 = opc2 = opc3 = 0

        time_text_surface = game_font.render(str(time_left), False,(255,255,255))
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        screen = pygame.display.set_mode((CONST.DISPLAY_SIZE_X, CONST.DISPLAY_SIZE_Y), pygame.FULLSCREEN)
        done = False
        clock = pygame.time.Clock()

        # loop principal
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit(0)
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        exit(0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        data_harvest.pressed_keys.append(['PRESS_K_UP',datetime.datetime.now()])
                        hero.shuffle_random_direction()
                    if event.key == pygame.K_DOWN: 
                        data_harvest.pressed_keys.append(['PRESS_K_DOWN',datetime.datetime.now()])
                        hero.shuffle_random_direction()
                    if event.key == pygame.K_LEFT: 
                        data_harvest.pressed_keys.append(['PRESS_K_LEFT',datetime.datetime.now()])
                        hero.shuffle_random_direction()
                    if event.key == pygame.K_RIGHT:
                        data_harvest.pressed_keys.append(['PRESS_K_RIGHT',datetime.datetime.now()])
                        hero.shuffle_random_direction()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        data_harvest.pressed_keys.append(['RELEASE_K_UP',datetime.datetime.now()])
                    if event.key == pygame.K_DOWN: 
                        data_harvest.pressed_keys.append(['RELEASE_K_DOWN',datetime.datetime.now()])
                    if event.key == pygame.K_LEFT: 
                        data_harvest.pressed_keys.append(['RELEASE_K_LEFT',datetime.datetime.now()])
                    if event.key == pygame.K_RIGHT:
                        data_harvest.pressed_keys.append(['RELEASE_K_RIGHT',datetime.datetime.now()])

                if event.type == pygame.USEREVENT:
                    if time_left > 0:
                        seconds=(pygame.time.get_ticks()-start_ticks)/1000
                        novo = (pygame.time.get_ticks()-start_ticks)/1000

                        if seconds < 8:
                            error_probability = 0
                        elif seconds < 25:
                            error_probability = random.randint(0,15)
                        elif seconds < 40:
                            error_probability = random.randint(0,11)
                        else:
                            error_probability = random.randint(0,7)
 
                        if error_probability == 1:
                            hero.zombie_scream()
                            hero.random_movement()

                        if error_probability == 2:
                            hero.zombie_scream()
                            hero.slow_down()
                         
                        if error_probability == 3:
                            hero.human_error()
                        #print(seconds)
                       # if seconds > 8:
                       #     bug_probability = random.randint(0,10)
                       #     #print("Bug Probability = " + str(bug_probability))
                       #     if bug_probability == 1:
                       #         bug = True
                       #     else:
                       #         bug = False
                       #     if (seconds % 5) == 0:
                       #         mirror = True
                       #         opc0 = random.randint(0,3)
                       #         opc1 = random.randint(0,3)
                       #         opc2 = random.randint(0,3)
                       #         opc3 = random.randint(0,3)
                       #         hero.zombie_error()
                       #     elif((novo % 4) == 0):
                       #         mirror = False
                        #countDown sound     
                        if (time_left == 6):
                            for i in range (0,6):
                                alreadySaid[i] = False
                        if (time_left == 6 and alreadySaid[time_left-1] == False):
                            countdown = pygame.mixer.Sound('src/sounds/5.wav')
                            countdown.play()
                            alreadySaid[time_left-1] = True
                        if (time_left == 5 and alreadySaid[time_left-1] == False) :
                            countdown = pygame.mixer.Sound('src/sounds/4.wav')
                            countdown.play()
                            alreadySaid[time_left-1] = True
                        if (time_left == 4 and alreadySaid[time_left-1] == False):
                            countdown = pygame.mixer.Sound('src/sounds/3.wav')
                            countdown.play()
                            alreadySaid[time_left-1] = True
                        if (time_left == 3 and alreadySaid[time_left-1] == False):
                            countdown = pygame.mixer.Sound('src/sounds/2.wav')
                            countdown.play()
                            alreadySaid[time_left-1] = True
                        if (time_left == 2 and alreadySaid[time_left-1] == False):
                            countdown = pygame.mixer.Sound('src/sounds/1.wav')
                            countdown.play()
                            alreadySaid[time_left-1] = True
                        if (time_left == 1 and alreadySaid[time_left-1] == False):
                            countdown = pygame.mixer.Sound('src/sounds/0.wav')
                            countdown.play()
                            time.sleep(0.5)
                            #alreadySaid[time_left-1] = True
                        time_left -= 1
                    else:
                        #print score
                        data_harvest.your_score.append(score)
                        if(score > placar):
                            data_harvest.best_score.append(score)
                            arq = open('src/placar.txt', 'w')
                            arq.write(str(score))
                            arq.close()
                            arq1 = open('src/nomeBest.txt', 'w')
                            arq1.write(data_harvest.name[0])
                            arq1.close()
                        else:
                            data_harvest.best_score.append(placar)

                        done = True

                        # salva os dados coletados
                        d = time.time()
                        dir_path = data_harvest.name + "-" + str(d)
                        os.makedirs('data/'+dir_path)
                        pd.DataFrame(data_harvest.pressed_keys).to_csv("data/"+dir_path+"/pressed_keys.csv",index=None,header=['PRESSED_KEY','TIME'])
                        pd.DataFrame(data_harvest.random_events).to_csv("data/"+dir_path+"/random_events.csv",index=None,header=['RANDOM_EVENT','TIME'])
                        pd.DataFrame(data_harvest.hero_movement).to_csv("data/"+dir_path+"/hero_movement.csv",index=None,header=['DIRECTION','SPEED','TIME'])
                        data_harvest.final_score = score
                        pd.DataFrame([data_harvest.final_score]).to_csv("data/"+dir_path+"/"+data_harvest.name,index=None,header=['SCORE'])
     
            
            # pega as teclas pressionadas
            pressed = pygame.key.get_pressed()
            #print(mirror)

            if pressed[pygame.K_ESCAPE]:
                quit(0)

            else:
                if pressed[pygame.K_UP]:
                    hero.move_up()
                elif pressed[pygame.K_DOWN]:
                    hero.move_down()
                elif pressed[pygame.K_LEFT]:
                    hero.move_left()
                elif pressed[pygame.K_RIGHT]:
                    hero.move_right()
            # checa se a bola está dentro do heroi
            if hero.has_ball_inside(ball):
                data_harvest.random_events.append(['ZOMBIE_EATS',datetime.datetime.now()])
                score += 1
                score_text_surface = game_font.render('Pontos: ' + str(score), False,(255,255,255))
                hero.bite()
                ball.set_random_position(hero)
                time_left += 2

            # atualiza o tempo
            if time_left < 6:
                time_text_surface = game_font.render(str(time_left), False,(255,0,0))
            else:
                time_text_surface = game_font.render(str(time_left), False,(255,255,255))

            screen.fill((0, 0, 0))
            screen.blit(background,(0,70))
            hero_group.update()
            hero_group.draw(screen)
            screen.blit(get_image('img/cerebro.png'), (ball.pos.x, ball.pos.y))
            screen.blit(score_text_surface,(CONST.DISPLAY_SIZE_X - 250,10))
            screen.blit(time_text_surface,(CONST.DISPLAY_SIZE_X/2 - 0,10))
            screen.blit(placar_text_surface,(CONST.DISPLAY_SIZE_X/2 - 450,30))
            pygame.display.flip()
            clock.tick(60)
