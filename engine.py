import pygame, math

class Scene:
    def __init__(self, screen, background_image=None, background_color=(20, 206, 215)):
        self.screen = screen
        self.background = pygame.image.load(background_image).convert_alpha() if background_image else None
        self.background_color = background_color
        self.offset = (0, 0)
        self.entities = []

    def add_entity(self, ID, entity):
        self.entities.append({ID: entity})
    
    def draw(self):
        self.screen.fill(self.background_color)
        if self.background:
            self.screen.blit(self.background, self.offset)
        for entity in self.entities:
            list(entity.values())[0].draw(self.screen, self.offset)

class Sprite:
    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.animations = {}
        self.current_animation = None
        self.current_frame = 0

    def load(self, image):
        self.render = pygame.transform.scale(image, (self.width, self.height))
        self.render = pygame.transform.rotate(self.render, self.angle)

    def add_animation(self, name, frames, speed=6):
        final_frames = []
        for frame in frames:
            for i in range(speed):
                final_frames.append(pygame.image.load(frame).convert_alpha())
        self.animations[name] = final_frames
        self.current_animation = name
        self.current_frame = 0
    
    def draw(self, screen, offset):
        if self.current_animation:
            self.load(self.animations[self.current_animation][self.current_frame])
            self.current_frame += 1
            if self.current_frame >= len(self.animations[self.current_animation]):
                self.current_frame = 0
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        rect.move_ip(offset)
        screen.blit(self.render, rect)
        