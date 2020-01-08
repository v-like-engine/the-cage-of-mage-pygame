import pygame

from load_image import load_image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__()
        self.x = x
        self.y = y
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
    def __init__(self, x, y, fps, box_group):
        super().__init__(load_image('mage pictures.png'), 8, 4, x, y)
        self.velocity = [0, 0]
        self.direction = 0
        self.v = 180 / fps
        self.g = 0
        self.up = False
        self.box_group = box_group
        self.mask = pygame.mask.from_surface(self.image)
        self.chest = None

    def update(self, event=None, v=0, *borders):
        self.change_coords(2, v, self.g)
        if not pygame.sprite.spritecollideany(self, borders[0]):
            self.velocity = self.velocity[0], 1
            self.g += 0.2
        else:
            self.change_coords(2, -v, self.g)
            self.velocity = self.velocity[0], 0
            self.g = 1
        if event.type == pygame.KEYDOWN:
            self.direction = -1
            if event.key == pygame.K_LEFT:
                self.direction = 1
                self.velocity = -1, self.velocity[1]
            if event.key == pygame.K_RIGHT:
                self.direction = 0
                self.velocity = 1, self.velocity[1]
            if event.key == pygame.K_UP and self.velocity[1] == 0 and not self.up:
                self.direction = -1
                self.velocity = self.velocity[0], -4
                self.up = True
            if self.direction != -1:
                self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
                frame = self.direction * 16 + self.cur_frame
                self.image = self.frames[frame]
                self.change_coords(0)
                if self.chest:
                    if frame in [15, 31] or pygame.sprite.spritecollideany(self, borders[1]) or \
                            pygame.sprite.collide_mask(self, self.chest):
                        self.velocity = -self.velocity[0], self.velocity[1]
                        self.change_coords(0)
                else:
                    if frame in [15, 31] or pygame.sprite.spritecollideany(self, borders[1]):
                        self.velocity = -self.velocity[0], self.velocity[1]
                        self.change_coords(0)
            # self.move(self.x, self.y + 10 / FPS)
        if event.type == pygame.KEYUP:
            self.up = False

    def change_coords(self, x_or_y, *g):
        if x_or_y == 0:
            self.rect.x += self.v * self.velocity[0]
            self.rect.y += self.v * self.velocity[1]
        elif x_or_y == 1:
            self.rect.x += self.v * self.velocity[0]
        else:
            self.rect.y += self.v * self.velocity[1] * g[0]
        self.x = self.rect.x
        self.y = self.rect.y

    def add_chest(self, chest):
        self.chest = chest