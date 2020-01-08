import pygame

from load_image import load_image
from simple_sprite import SimpleSprite


class Chest(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        self.image = load_image('chest.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, event=None, v=0, *borders):
        pass