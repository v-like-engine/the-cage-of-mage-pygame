import pygame

from utils import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, image_name):
        super().__init__()
        self.image = load_image(image_name)
        self.rect = self.image.get_rect()