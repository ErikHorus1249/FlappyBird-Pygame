
import pygame, sys

# khoi tao pygame
pygame.init()

# thong so cho khung canvas
WIDTH, HEIGHT = 400, 710
clock = pygame.time.Clock()
gravity = 0.25


# bien FPS
FPS = 120

# hien thi khung canvas
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# anh cho background
bg_surface = pygame.transform.scale(pygame.image.load('img/background-day.png').convert(),(WIDTH,HEIGHT))

# anh cho phan nen
floor_surface = pygame.image.load('img/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# con chim
bird_surface = pygame.image.load('img/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (110, 512))
bird_movement = 0
# chuyen dong nen dat
def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, HEIGHT - 100))
    # screen.blit(floor_surface, (floor_x_pos + 590, HEIGHT - 100))


# Vong lap chinh cua game
while True:
    # thiet lap thoat game
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_SPACE:
               bird_movement = 0
               bird_movement -= 10


    screen.blit(bg_surface, (0, 0))
    bird_movement += gravity
    # Thay doi gia tri y cua con chim
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect)
    # hieu ung chuyen dong nen
    floor_x_pos -= 1
    draw_floor()
    # neu nhu thanh nen chay het ra ngoai canvas thi reset lai vi tri
    if(floor_x_pos < -100):
        floor_x_pos = 0

    # update
    pygame.display.update()
    # FPS
    clock.tick(FPS)