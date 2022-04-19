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
            entity.draw(self.screen, self.offset)

class Entity:
    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect = pygame.transform.rotate(self.rect, self.angle)
    
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.rect = pygame.transform.rotate(self.rect, self.angle)
    
    def return_rect(self, offset):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        rect = pygame.transform.rotate(self.rect, self.angle)
        rect.move_ip(offset)
        return rect

class Rectangle(Entity):
    def __init__(self, x, y, width, height, angle, color=(0, 0, 0)):
        super().__init__(x, y, width, height, angle)

    def draw(self, screen, offset):
        rect = self.return_rect(offset)
        pygame.draw.rect(screen, self.color, rect)

class Ellipse(Entity):
    def __init__(self, x, y, width, height, angle, color=(0, 0, 0)):
        super().__init__(x, y, width, height, angle)

    def draw(self, screen, offset):
        rect = self.return_rect(offset)
        pygame.draw.ellipse(screen, self.color, rect)

class Line(Entity):
    def __init__(self, x, y, width, height, angle, color=(0, 0, 0)):
        super().__init__(x, y, width, height, angle)

    def draw(self, screen, offset):
        rect = self.return_rect(offset)
        pygame.draw.line(screen, self.color, (rect.x, rect.y), (rect.x + rect.width, rect.y + rect.height))

