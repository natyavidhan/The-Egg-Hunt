import pygame, math, os, json

class Scene:
    def __init__(self, screen, _game_map, background_image=None, background_color=(20, 206, 215)):
        self.screen = screen
        self.background = pygame.image.load(background_image).convert_alpha() if background_image else None
        self.background_color = background_color
        self.offset = (0, 0)
        self.entities = []
        self.game_map = _game_map

    def add_entity(self, ID, entity):
        self.entities.append({ID: entity})

    def draw(self):
        self.screen.fill(self.background_color)
        if self.background:
            self.screen.blit(self.background, self.offset)
        for i in self.game_map.game_map:
            x, y, tile = i
            self.screen.blit(tile, (x, y, 32, 32))
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

class SceneMap:
    def __init__(self, map_json_file, tiles_directory):
        self.json_map = json.load(open(map_json_file))
        layers = {}

        _grass_tiles = os.listdir(tiles_directory)
        self.tiles = []
        for i in _grass_tiles:
            self.tiles.append(pygame.image.load(f"{tiles_directory}/{i}"))

        self.game_map = []
        for layer in self.json_map["layers"]:
            _x, _y, i = 0, 0, 0
            for e in layer["data"]:
                if e != 0:
                    self.game_map.append([_x, _y, self.tiles[e-1]])
                _x+=32
                i+=1
                if i > layer["width"]-1:
                    i=0
                    _x = 0
                    _y+=32
