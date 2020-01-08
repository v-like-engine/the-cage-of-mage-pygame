from background_sprites import Background, Border
from box import Box
from hero_classes import Mage

import pygame

FPS = 30
WIDTH = 1280
HEIGHT = 720
pygame.init()
pygame.mixer_music.load('data/Kytami-Sirens.mp3')
pygame.mixer_music.play(0, 0.0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
ticks = 0
all_sprites = pygame.sprite.Group()
mage_group = pygame.sprite.Group()
border_b = pygame.sprite.Group()
borders = pygame.sprite.Group()
box_group = pygame.sprite.Group()


training_background = Background('training.jpg', 0, -30)
training_background.add(all_sprites)
border_bottom = Border(1280, 64, 0, 656)
border_bottom.add(border_b)
border_left = Border(32, 720, 0, 0)
border_right = Border(32, 720, 1248, 0)
border_left.add(borders)
border_right.add(borders)
mage = Mage(50, 0)
mage.add(all_sprites)
mage.add(mage_group)
pygame.key.set_repeat(10)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            mage.update(event, 10, border_b, borders)
        if event.type == pygame.MOUSEBUTTONDOWN:
            box = Box(box_group, screen, *event.pos, mage)
            box_group.add(box)
    screen.fill(pygame.Color("#383636"))
    all_sprites.draw(screen)
    border_b.draw(screen)
    borders.draw(screen)
    box_group.draw(screen)
    mage_group.draw(screen)
    mage_group.update(event, 10, border_b, borders)
    box_group.update(event, 10, border_b, borders)
    pygame.display.flip()
    clock.tick(FPS)
    ticks += 1

pygame.quit()
