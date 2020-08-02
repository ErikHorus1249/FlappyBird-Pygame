
import pygame, sys

pygame.init()

WIDTH, HEIGHT = 500, 700
clock = pygame.time.Clock()
FPS = 120
screen = pygame.display.set_mode((WIDTH,HEIGHT))

bg_surface = pygame.transform.scale(pygame.image.load('img/background-day.png').convert(),(WIDTH,HEIGHT))

floor_surface = pygame.image.load('img/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, HEIGHT - 100))
    screen.blit(floor_surface, (floor_x_pos + 590, HEIGHT - 100))

while True:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg_surface, (0, 0))
    floor_x_pos -= 1
    draw_floor()
    if(floor_x_pos < -600):
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(FPS)