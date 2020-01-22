import pygame

from utils.load_image import load_image


class Door(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group)
        self.x = x
        self.y = y
        self.simple_image = load_image('door_frame.png')
        self.opened = load_image('door1.png')
        self.simple_image = pygame.transform.scale(self.simple_image, (40, 320))
        self.image = self.simple_image
        self.w = self.image.get_width()
        self.h = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_opened = False

    def open(self):
        if not self.is_opened:
            self.image = self.opened
        else:
            self.image = self.simple_image
        self.is_opened = not self.is_opened
        print(self.is_opened)

    def move_frame(self, x_diff, y_diff):
        self.rect.x += x_diff
        self.rect.y += y_diff
        self.x = self.rect.x
        self.y = self.rect.y
