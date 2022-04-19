import pygame

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("The Egg Hunt")
clock = pygame.time.Clock()
RUNNING = True

while RUNNING:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    screen.fill((20, 206, 215))
    pygame.display.flip()
