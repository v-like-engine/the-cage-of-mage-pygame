import pygame

from load_image import load_image


class Door(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group)
        self.x = x
        self.y = y
        self.simple_image = load_image('door_frame.png')
        self.opened = load_image('door.png')
        self.image = self.simple_image
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_opened = False

    def open(self):
        self.image = self.opened
        self.is_opened = True