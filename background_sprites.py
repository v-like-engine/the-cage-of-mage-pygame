import pygame

from utils import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, image_name, move_x, move_y):
        super().__init__()
        self.image = load_image(image_name)
        self.rect = self.image.get_rect().move(move_x, move_y)


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.rect = self.image.get_rect().move(move_x, move_y)
        pygame.draw.rect(self.image, pygame.Color(0, 0, 0), (move_x, move_y, x, y))
