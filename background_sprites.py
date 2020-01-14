import pygame

from load_image import load_image


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
        self.coords = move_x, move_y, move_x + x, move_y + y
        pygame.draw.rect(self.image, pygame.Color('black'), (move_x, move_y, move_x + x, move_y + y))
        self.image.set_alpha(0)
