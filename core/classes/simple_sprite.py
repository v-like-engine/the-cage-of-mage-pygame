import pygame

class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group)
        self.screen = screen
        self.x = x
        self.y = y
