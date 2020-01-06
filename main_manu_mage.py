import pygame

from load_image import load_image


class MainMenuMage(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group)
        self.group = group
        self.screen = screen
        self.x = x
        self.y = y
        self.image = load_image('mage-with-torch.png')
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y