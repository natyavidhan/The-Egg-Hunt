import pygame, os, json
import engine, objects

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("The Egg Hunt")
clock = pygame.time.Clock()
RUNNING = True


game_map = engine.SceneMap("maps/level_1.json", "assets/terrain")
level_1 = engine.Scene(screen, game_map)
player = objects.Player(100, 100, 64, 64, 0)
player.add_animation("idle", ["assets/chick 1.png"])
player.add_animation(
    "walk",
    [
        "assets/chick 1.png",
        "assets/chick 2.png",
        "assets/chick 3.png",
        "assets/chick 2.png",
    ],
)
player.current_animation = "idle"
level_1.add_entity("player", player)

while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    level_1.scroll(player)
    level_1.draw()
    player.update(level_1)
    pygame.display.flip()
