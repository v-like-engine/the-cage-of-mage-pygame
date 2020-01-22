import pygame

from utils.load_image import load_image


class Background(pygame.sprite.Sprite):
    def __init__(self, image_name, move_x, move_y):
        super().__init__()
        self.image = load_image(image_name)
        self.rect = self.image.get_rect().move(move_x, move_y)

    def move_frame(self, x_diff, ydiff):
        self.rect.x += x_diff
        self.rect.y += ydiff


class Border(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y):
        super().__init__()
        self.image = pygame.Surface([x, y])
        self.rect = self.image.get_rect().move(move_x, move_y)
        self.coords = move_x, move_y, move_x + x, move_y + y
        pygame.draw.rect(self.image, pygame.Color('black'), (move_x, move_y, move_x + x, move_y + y))
        self.image.set_alpha(0)

    def move_frame(self, x_diff, y_diff):
        self.rect.x += x_diff
        self.rect.y += y_diff


class Decoration(pygame.sprite.Sprite):
    def __init__(self, image_name, move_x, move_y, *size):
        super().__init__()
        self.image = load_image(image_name)
        if size:
            self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect().move(move_x, move_y)

    def move_frame(self, x_diff, y_diff):
        self.rect.x += x_diff
        self.rect.y += y_diff


class Message(pygame.sprite.Sprite):
    def __init__(self, image_name, move_x, move_y, rotate=0, *size):
        super().__init__()
        self.image = load_image(image_name)
        if size:
            self.image = pygame.transform.scale(self.image, size)
        if rotate != 0:
            self.image = pygame.transform.rotate(self.image, rotate)
        self.rect = self.image.get_rect().move(move_x, move_y)

    def move_frame(self, x_diff, y_diff):
        self.rect.x += x_diff
        self.rect.y += y_diff
