import pygame

from platform_load import Platform


class MovingPlatform(Platform):
    def __init__(self, group, image, screen, x, y, start_x, start_y, moving_x, moving_y, speed):
        self.image = pygame.transform.rotate(image, 90)
        super().__init__(group, self.image, screen, x, y)
        self.screen = screen
        self.h = self.image.get_height()
        self.start_x = start_x
        self.start_y = start_y
        self.moving_x = moving_x
        self.moving_y = moving_y
        self.screen_height = self.screen.get_height()
        self.up = False
        self.right = False
        self.speed = speed

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def change_speed(self, speed):
        self.speed = speed

    def update(self):
        if self.start_y != self.moving_y:
            if self.rect.y >= self.start_y and not self.up:
                self.up = True
                self.set_pos(self.rect.x, self.rect.y + self.speed)
            elif self.rect.y <= self.moving_y and self.up:
                self.up = False
                self.set_pos(self.rect.x, self.rect.y - self.speed)
            elif self.up:
                self.set_pos(self.rect.x, self.rect.y - self.speed)
            else:
                self.set_pos(self.rect.x, self.rect.y + self.speed)
        if self.start_x != self.moving_x:
            if self.rect.x <= self.start_y and not self.right:
                self.right = True
                self.set_pos(self.rect.x - self.speed, self.rect.y)
            elif self.rect.x >= self.moving_x and self.right:
                self.right = False
                self.set_pos(self.rect.x + self.speed, self.rect.y)
            elif self.right:
                self.set_pos(self.rect.x + self.speed, self.rect.y)
            else:
                self.set_pos(self.rect.x - self.speed, self.rect.y)
