import pygame
import engine

class Player(engine.Sprite):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.origin = (self.width//2, self.height//2)
    
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def update(self):
        self.move()
        self.x += self.direction.x * self.speed
        self.y += self.direction.y * self.speed