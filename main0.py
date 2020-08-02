
import pygame, sys

pygame.init()

WIDTH, HEIGHT = 400, 712
clock = pygame.time.Clock()
FPS = 120
screen = pygame.display.set_mode((WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    pygame.display.update()
    clock.tick(FPS)