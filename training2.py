from temporary_check import Skelet

import pygame

FPS = 15
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
ticks = 0
all_sprites = pygame.sprite.Group()
mage_group = pygame.sprite.Group()


mage = Skelet(0, 0)
mage.add(all_sprites)
pygame.key.set_repeat(10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            mage.update(event)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    mage_group.draw(screen)
    mage_group.update()
    pygame.display.flip()
    clock.tick(FPS)
    ticks += 1

pygame.quit()