import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, group, image, screen, x, y):
        super().__init__(group)
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect = pygame.Rect(self.x, self.y - 5, self.image.get_width(), self.image.get_height())