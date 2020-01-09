import pygame

from load_image import load_image
from simple_sprite import SimpleSprite


class Chair(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        print('кря')
        self.image = load_image('chair.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y