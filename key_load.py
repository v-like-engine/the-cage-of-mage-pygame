import pygame

from load_image import load_image
from simple_sprite import SimpleSprite


class Key(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        self.image = load_image('key.png')
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (self.w // 10, self.h // 10))
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y