import pygame

class Scene:
    def __init__(self, screen, background_image=None, background_color=(20, 206, 215)):
        self.screen = screen
        self.background = pygame.image.load(background_image).convert_alpha() if background_image else None
        self.background_color = background_color
        self.offset = (0, 0)
        self.entities = []

    def add_entity(self, entity):
        self.entities.append(entity)
    
    def draw(self):
        self.screen.fill(self.background_color)
        if self.background:
            self.screen.blit(self.background, self.offset)
        for entity in self.entities:
            entity.draw(self.screen, self.offset)