import pygame

from load_image import load_image


class ScreenEffect(pygame.sprite.Sprite):
    def __init__(self, image_name, move_x, move_y):
        super().__init__()
        self.image = load_image(image_name)
        self.rect = self.image.get_rect().move(move_x, move_y)

    def move_frame(self, x_diff, ydiff):
        self.rect.x += x_diff
        self.rect.y += ydiff
