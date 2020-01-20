import pygame

from platform_load import Platform


class MovingPlatform(Platform):
    def __init__(self, group, image, screen, x, y, step):
        self.image = pygame.transform.rotate(image, 90)
        super().__init__(group, self.image, screen, x, y)
        self.screen = screen
        self.h = self.image.get_height()
        self.screen_height = self.screen.get_height()
        self.up = False
        self.step = step

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def update(self):
        if self.rect.y >= 470 and not self.up:
            self.up = True
            self.set_pos(self.rect.x, self.rect.y + self.step)
        elif self.rect.y <= 50 and self.up:
            self.up = False
            self.set_pos(self.rect.x, self.rect.y - self.step)
        elif self.up:
            self.set_pos(self.rect.x, self.rect.y - self.step)
        else:
            self.set_pos(self.rect.x, self.rect.y + self.step)