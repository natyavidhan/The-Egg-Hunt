import pygame
import engine


class Player(engine.Sprite):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 75
        self.origin = (self.width // 2, self.height // 2)
        self.gravity = 0.6
        self.jump_speed = -400
        self.in_air = False

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.body.velocity = (self.speed, self.body.velocity[1])
            self.flipped = False
            self.current_animation = "walk"
        elif keys[pygame.K_a]:
            self.body.velocity = (-self.speed, self.body.velocity[1])
            self.flipped = True
            self.current_animation = "walk"
        else:
            self.body.velocity = (0, self.body.velocity[1])
            self.current_animation = "idle"
        if keys[pygame.K_w]:
            if not self.in_air:
                self.body.velocity = (self.body.velocity[0], self.jump_speed)
                self.in_air = True

    def update(self, scene: engine.Scene):
        self.move()
        tiles = scene.game_map.rects
        for tile in tiles:
            if self.rect.colliderect(tile):
                self.in_air = False
                break
        player_rect = scene.entities[0]["player"].rect
        scene.screen.blit(self.render, self.rect)
