import pygame
from sys import exit

pygame.init()
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert()
graphics = pygame.image.load('graphics/ground.png').convert()
text_surface = text_font.render('My game', False, 'Green').convert()

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(graphics, (0, 300))
    screen.blit(text_surface, (350, 50))
    screen.blit(player_surf, (0, 215))
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    pygame.display.update()
    clock.tick(60)

