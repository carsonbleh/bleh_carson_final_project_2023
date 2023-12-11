# This file was created by: Carson Bleh

import pygame
import random

class Player(pygame.sprite.Sprite):
    # setting up the player
    def __init__(self, SnakePos, SnakeBod, SnakeDir, SnakeSpeed):
        super().__init__()
        self.position = SnakePos
        self.Snake = SnakeBod
        self.direction = SnakeDir
        self.MoveDirection = SnakeDir
        self.Speed = SnakeSpeed

    # assigning keys to direction changes
    def directionChange(self, dir):
        if dir == "RIGHT" and not self.direction == "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and not self.direction == "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and not self.direction == "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and not self.direction == "UP":
            self.direction = "DOWN"

    # move function, constantly extends player by 5 coordinates
    # stops the player from constantly extending
    def move(self, Block):
        if self.direction == "RIGHT":
            self.position[0] += self.Speed
        if self.direction == "LEFT":
            self.position[0] -= self.Speed
        if self.direction == "UP":
            self.position[1] -= self.Speed
        if self.direction == "DOWN":
            self.position[1] += self.Speed
        # This inserts the position to the snakes body when snake hits the block
        # If snake doesnt hit food, the last element of the body is removed stopping the snake getting constantly longer
        self.Snake.insert(0, list(self.position))
        # This translates the apples position from one point in the middle to the whole image
        # abs = absolute value of the x and y distances
        if abs(self.position[0] -Block[0]) < 15 and abs(self.position[1] -Block[1]) < 15:
            return 1
        else:
            self.Snake.pop()
            return 0
    
    # Game ending moves
    # If player runs out of the dimensions of the screen or if the head of the snakes connects with the body
    def Collisions(self):
        if self.position[0] > 485 or self.position[0] < 0:
            return 1
        elif self.position[1] > 485 or self.position[1] < 0:
            return 1
        for SnakeSection in self.Snake[1:]:
            if self.position == SnakeSection:
                return 1
        return 0

    def SnakeHead(self):
        return self.position

    def SnakeBody(self):
        return self.Snake

# Class for the snake food
class Apple:
    # Initial characteristics of the food
    # Use random function to place object somewhere on the screen dimensions
    def __init__(self):
        self.position = [random.randrange(10, 450), random.randrange(10, 450)]
        self.BlocksInScreen = True

    # Whenever blocks are run into, a new one is randomly sent to screen
    def GenerateBlock(self):
        if not self.BlocksInScreen:
            self.position = [random.randrange(10, 450), random.randrange(10, 450)]
            self.BlocksInScreen = True
        return self.position

    def Blocks(self, b):
        self.BlocksInScreen = b

