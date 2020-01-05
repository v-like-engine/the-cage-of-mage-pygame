import pygame

from utils import load_image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.animation_fps = 10
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(x, y)
        self.direction = 0

    def cut_sheet(self, sheet, columns, rows):
        width = sheet.get_width() // columns
        height = sheet.get_height() // rows
        for j in range(rows):
            for i in range(columns):
                x = width * i
                y = height * j
                self.frames.append(sheet.subsurface(x, y, width, height))

    def update(self):
        pass


class Mage(AnimatedSprite):
    def __init__(self, x, y):
        super().__init__(load_image('mage pictures.png'), 8, 4, x, y)
        self.velocity = [0, 0]
        self.direction = 0

    def update(self, event=None, *borders):
        if not event:
            return
        if event.type == pygame.KEYDOWN:
            self.direction = -1
            if event.key == pygame.K_LEFT:
                self.direction = 1
                self.velocity = -1, 0
            if event.key == pygame.K_RIGHT:
                self.direction = 0
                self.velocity = 1, 0
            if self.direction != -1:
                self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
                frame = self.direction * 16 + self.cur_frame
                self.image = self.frames[frame]
                if frame not in [15, 31]:
                    if borders:
                        if len(borders) == 4:
                            if borders[1] > 10 * self.velocity[0] + self.rect.x > borders[0]:
                                self.change_coords(1, 10)
                            if borders[3] > 10 * self.velocity[1] + self.rect.x > borders[2]:
                                self.change_coords(2, 10)
                        else:
                            self.change_coords(0, 10)
                    else:
                        self.change_coords(0, 10)

    def change_coords(self, x_or_y, step):
        if x_or_y == 0:
            self.rect.x += step * self.velocity[0]
            self.rect.y += step * self.velocity[1]
        elif x_or_y == 1:
            self.rect.x += step * self.velocity[0]
        else:
            self.rect.y += step * self.velocity[1]
