import pygame
import engine

class Player(engine.Sprite):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)
