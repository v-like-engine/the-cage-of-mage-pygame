import pygame

from utils.load_image import load_image
from core.classes.simple_sprite import SimpleSprite


class Chair(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        print('не кря')
        self.image = load_image('chair.png')
        self.image = pygame.transform.scale(self.image, (120, 120))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
