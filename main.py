import pygame, os, json
import engine

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("The Egg Hunt")
clock = pygame.time.Clock()
RUNNING = True


game_map = json.load(open("maps/level_1.json"))
level_1 = engine.Scene(screen, game_map)
player = engine.Sprite(100, 100, 64, 64, 0)
player.add_animation("idle", [os.path.join('assets', "chick 1.png")])
player.add_animation("walk", [os.path.join('assets', "chick 1.png"), os.path.join('assets', "chick 2.png"),
                            os.path.join('assets', "chick 3.png"), os.path.join('assets', "chick 2.png")])
player.current_animation = "idle"
level_1.add_entity("player", player)

while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    level_1.draw()
    pygame.display.flip()
