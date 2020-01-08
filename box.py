import pygame

from load_image import load_image
from simple_sprite import SimpleSprite


class Box(SimpleSprite):
    def __init__(self, group, screen, x, y, mage):
        super().__init__(group, screen, x, y)
        self.image = load_image('box.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.g = 1
        self.velocity = [0, 0]
        self.direction = 0
        self.mage = mage
        self.a = 10

    def update(self, event=None, v=0, *borders):
        self.change_coords(2, v, self.g)
        if not pygame.sprite.spritecollideany(self, borders[0]):
            self.velocity = self.velocity[0], 1
            self.g += 0.2
        else:
            self.change_coords(2, -v, self.g)
            self.velocity = self.velocity[0], 0
            self.g = 1
        if self.mage.x + 70 >= self.x and self.mage.y + self.mage.rect.height == self.y + self.rect.height:
            self.direction = 0
            self.velocity = 1, self.velocity[1]
        else:
            self.direction = -1
            self.velocity = 0, self.velocity[1]
        if self.direction != -1:
            self.change_coords(0, 10)
            if pygame.sprite.spritecollideany(self, borders[1]):
                self.change_coords(0, -10)

    def change_coords(self, x_or_y, step, *g):
        if x_or_y == 0:
            self.rect.x += step * self.velocity[0]
            self.rect.y += step * self.velocity[1]
        elif x_or_y == 1:
            self.rect.x += step * self.velocity[0]
        else:
            self.rect.y += step * self.velocity[1] * g[0]
        self.x = self.rect.x
        self.y = self.rect.y