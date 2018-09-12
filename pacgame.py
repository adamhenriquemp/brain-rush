# -*- encoding:utf-8 -*-
import pygame
import time
#import pandas as pd
from src.game_window import GameWindow
from src.end_window import EndWindow
from src.menu_window import MenuWindow

#pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('src/sounds/back.mp3')
pygame.mixer.music.play(0)
pygame.mixer.music.set_volume(0.5)

menu_window = MenuWindow()
game_window  = GameWindow()
end_window  = EndWindow()
