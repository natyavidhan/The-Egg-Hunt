import pygame
import engine


class Player(engine.Sprite):
    def __init__(self, x, y, width, height, angle):
        super().__init__(x, y, width, height, angle)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5
        self.origin = (self.width // 2, self.height // 2)
        self.gravity = 0.6
        self.jump_speed = -10

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x = 1
            self.flipped = False
            self.current_animation = "walk"
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.flipped = True
            self.current_animation = "walk"
        else:
            self.direction.x = 0
            self.current_animation = "idle"
        if keys[pygame.K_w]:
            self.direction.y = self.jump_speed

    def update(self, scene: engine.Scene):
        self.move()
        # self.direction.y += self.gravity
        tiles = scene.game_map.bodies
        player_rect = scene.entities[0]["player"].rect
        pygame.draw.rect(scene.screen, (255, 0, 0), player_rect, 1)

        # self.x += self.direction.x * self.speed
        # self.y += self.direction.y

        # if self.x < 0 + self.width / 2:
        #     self.x = 0 + self.width / 2
        # elif self.x > scene.game_map.width - self.width / 2:
        #     self.x = scene.game_map.width - self.width / 2

        # self.y += self.direction.y
        scene.screen.blit(self.render, self.rect)
