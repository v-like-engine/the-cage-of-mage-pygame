from background_sprites import Background
from hero_classes import Mage

import pygame

FPS = 30
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
ticks = 0
all_sprites = pygame.sprite.Group()
mage_group = pygame.sprite.Group()


training_background = Background('training.jpg')
training_background.add(all_sprites)
mage = Mage(50, 450)
mage.add(all_sprites)
mage.add(mage_group)
pygame.key.set_repeat(10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            mage.update(event, 20, 1110, 50, 450)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    mage_group.draw(screen)
    mage_group.update()
    pygame.display.flip()
    clock.tick(FPS)
    ticks += 1

pygame.quit()