# This file was created by: Carson Bleh

'''
Final project: snake video game - recreation of google snake game
Goals:
Introduction and game end screen
Ability to pause game
Single player
Game ends when snake hits wall or hits itself
Gain points when snake eats apple
'''

'''
Sources:
[Chris Bradfield - Kids can code](https://kidscancode.org/)
[freeCodeCamp.org](https://www.youtube.com/watch?v=8dfePlONtls)
[Coder Space](https://www.youtube.com/watch?v=_-KjEgCLQFw)
[Wajiha Urooj](https://www.edureka.co/blog/snake-game-with-pygame/)
[Stack Overflow](https://stackoverflow.com/questions/33537959/continuous-movement-of-a-box-in-pygame)
'''

import pygame
import random
from sprites import *
import os
pygame.init()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'images')

#images
Background = pygame.image.load(os.path.join('images','BG2.png'))
SnakeFood = pygame.image.load(os.path.join('images','Apple2.png'))


# set colors using rgb values
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

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

# Function to pause game
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

# Generating the start (Intro) page of the game
# Two elements - adding text to screen and advancing to game with for loop.
def Intro():
    while True:
        Screen.blit(Background, (0, 0))
        IntroFont = pygame.font.SysFont("comicsansms", 20)
        IntroFont1 = pygame.font.SysFont("comicsansms", 40)
        msg1 = IntroFont1.render("WELCOME TO SNAKES", 1, WHITE)
        msg2 = IntroFont.render("Collect The Apples", 1, WHITE)
        msg3 = IntroFont.render("Press 1 to Play", 1, WHITE)

        Screen.blit(msg1, (25, 100))
        Screen.blit(msg2, (155, 150))
        Screen.blit(msg3, (175, 250))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEnd()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    SinglePlayer()


# Main Loop
def SinglePlayer():
    score = 0
    while True:
        # for loop defining all the user actions with the event.get() function
        # All actions involving pressing a key are within a KEYDOWN loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GameEnd()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.directionChange("RIGHT")
                elif event.key == pygame.K_a:
                    player.directionChange("LEFT")
                elif event.key == pygame.K_w:
                    player.directionChange("UP")
                elif event.key == pygame.K_s:
                    player.directionChange('DOWN')
                elif event.key == pygame.K_p:
                    Pause(SinglePlayer)
        FoodBlocks = Food.GenerateBlock()
        # When Player collides with food, score increases
        if player.move(FoodBlocks):
            Food.Blocks(False)
            score += 1
        # Adding the background and apple to the screen
        Screen.blit(Background, (0, 0))
        Screen.blit(SnakeFood, Food.position)

        # Drawing the player to the screen
        for section in player.SnakeBody():
            pygame.draw.rect(Screen, WHITE, pygame.Rect(section[0], section[1], 15, 15))


        # If statement triggered after a Game ending collision, Player score is displayed on Screen
        # Screen updated and time delay added to display score for 2 seconds
        if player.Collisions():
            EndStatement()
            MyFont = pygame.font.SysFont("Helvetica", 40)
            YourScore = MyFont.render("Your Score: " + str(score), 1, WHITE)
            Screen.blit(YourScore, (120, 250))

            pygame.display.flip()
            pygame.time.delay(2000)
            GameEnd()

        # Messages displayed on the screen all the way through the game
        MyFont1 = pygame.font.SysFont("Helvetica", 15)
        ScoreBoard1 = MyFont1.render("Score: " + str(score), 1, BLACK)
        PauseMessage = MyFont1.render("Press P to Pause", 1, BLACK)
        Screen.blit(ScoreBoard1, (200, 10))
        Screen.blit(PauseMessage, (10, 10))
        pygame.display.set_caption('Snake Game')
        pygame.display.update()
        pygame.display.flip()
        # Determining Frame Rate and thus speed of players on the screen
        x = 30
        # if score % 5:
            # player.Speed += 1
        fps.tick(x)


Intro()