# This file was created by: Carson Bleh

'''
Final project: snake video game - recreation of google snake game
Goals:
Introduction and game end screen
Ability to pause game
Single player and two player mode
Game ends when snake hits wall
Gain points when snake eats apple
'''

import pygame
import random
from sprites import *
pygame.init()

# set colors using rgb values
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# images
Background = pygame.image.load('BG.jpg')
SnakeFood = pygame.image.load('Apple2.png')

# set screen Dimensions
ScreenWidth = 500
ScreenHeight = 500
Screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

fps = pygame.time.Clock()

def GameEnd():
    pygame.quit()

def EndStatement():
    # Closing Statement 
    # Implemented a time delay so message is displayed for longer time
    pygame.font.init()
    MyFont = pygame.font.SysFont("Helvetica", 50)
    EndText = MyFont.render("GAME OVER", 1, BLUE)
    Screen.blit(EndText, (100, 100))
    pygame.display.flip()
    pygame.time.delay(1000)

# assigning the initial characteristics of each sprite in the game
player = Player([250, 400], [[100, 50], [90, 50], [80, 50]], "UP", 6)
player1 = Player([250, 100], [[100, 50], [90, 50], [80, 50]], "DOWN", 6)
Food = Apple()

# Function to allow game to be paused
def Pause(ReturnToGame):
    while True:
        Screen.blit(Background, (0, 0))
        PauseFont = pygame.font.SysFont("comicsansms", 20)
        PauseFont1 = pygame.font.SysFont("comicsansms", 40)
        msg1 = PauseFont1.render("Game Paused", 1, WHITE)
        msg2 = PauseFont.render("Press C to Continue", 1, WHITE)
        msg3 = PauseFont.render("Press Q to Quit", 1, WHITE)

        Screen.blit(msg1, (130, 100))
        Screen.blit(msg2, (155, 200))
        Screen.blit(msg3, (165, 250))
        pygame.display.update()

        # for loop allowing user to quit or continue game by pressing a corresponding button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEnd()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
                if event.key == pygame.K_q:
                    GameEnd()