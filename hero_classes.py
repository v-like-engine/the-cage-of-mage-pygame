import pygame

from load_image import load_image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *resize):
        super().__init__()
        self.x = x
        self.y = y
        self.frames = []
        resize = resize or False
        self.cut_sheet(sheet, columns, rows, resize)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect().move(x, y)
        self.direction = 0

    def cut_sheet(self, sheet, columns, rows, resize):
        width = sheet.get_width() // columns
        height = sheet.get_height() // rows
        for j in range(rows):
            for i in range(columns):
                x = width * i
                y = height * j
                image = sheet.subsurface(x, y, width, height)
                if resize:
                    image = pygame.transform.scale(image, resize)
                self.frames.append(image)

    def update(self):
        pass


class Mage(AnimatedSprite):
    def __init__(self, x, y, fps, *box_group):
        self.height = 240
        self.width = 160
        super().__init__(load_image('mage_pictures.png'), 8, 4, x, y, self.width, self.height)
        self.velocity = [0, 0]
        self.direction = 0
        self.game_fps = fps
        self.frame_fps = 40 / fps
        self.until_frame = 0
        self.v = 240 / fps
        self.mass_defined_v = 180 / fps
        self.g = 0.1
        self.up = False
        if box_group:
            self.box_group = box_group
        self.mask = pygame.mask.from_surface(self.image)
        self.chest = None

    def update(self, event=None, *borders):
        dno = borders[0].sprites()[0].coords[1]
        self.change_coords(2, dno)
        if not pygame.sprite.spritecollideany(self, borders[0]) and self.up:
            self.velocity = self.velocity[0], self.velocity[1] + self.g
        else:
            self.change_coords(2, dno)
            self.velocity = self.velocity[0], 0
            self.up = False
        if event.type == pygame.KEYDOWN:
            self.direction = -1
            if event.type == pygame.KEYDOWN and pygame.key.get_mods() & pygame.KMOD_LSHIFT:
                if event.key == pygame.K_LEFT:
                    self.v = 360 / self.game_fps
                    self.frame_fps = 60 / self.game_fps
                    self.direction = 1
                    self.velocity = -1, self.velocity[1]
                if event.key == pygame.K_RIGHT:
                    self.v = 360 / self.game_fps
                    self.frame_fps = 60 / self.game_fps
                    self.direction = 0
                    self.velocity = 1, self.velocity[1]
            elif event.key == pygame.K_LEFT:
                self.v = 240 / self.game_fps
                self.frame_fps = 40 / self.game_fps
                self.direction = 1
                self.velocity = -1, self.velocity[1]
            elif event.key == pygame.K_RIGHT:
                self.v = 240 / self.game_fps
                self.frame_fps = 40 / self.game_fps
                self.direction = 0
                self.velocity = 1, self.velocity[1]
            if event.key == pygame.K_UP and self.velocity[1] == 0 and not self.up:
                self.up = True
                self.v = 240 / self.game_fps
                self.frame_fps = 40 / self.game_fps
                self.direction = -1
                self.velocity = self.velocity[0], -5
                print('up', self.rect.y)
            if self.direction != -1:
                if self.until_frame > 0.98:
                    self.cur_frame = (self.cur_frame + 1) % (len(self.frames) // 2)
                    self.until_frame = 0
                else:
                    self.until_frame += self.frame_fps
                frame = self.direction * 16 + self.cur_frame
                self.image = self.frames[frame]
                self.change_coords(1)
                if self.chest:
                    if frame in [15, 31] or pygame.sprite.spritecollideany(self, borders[1]) or \
                            pygame.sprite.collide_mask(self, self.chest):
                        self.velocity = -self.velocity[0], self.velocity[1]
                        self.change_coords(1)
                else:
                    if frame in [15, 31] or pygame.sprite.spritecollideany(self, borders[1]):
                        self.velocity = -self.velocity[0], self.velocity[1]
                        self.change_coords(1)
            # self.move(self.x, self.y + 10 / FPS)

    def change_coords(self, x_or_y, *limits):
        if x_or_y in (0, 1):
            self.rect.x += self.v * self.velocity[0]
        elif x_or_y in (0, 2):
            if limits:
                if limits[0] >= self.rect.y - self.height + self.mass_defined_v * self.velocity[1]:
                    self.rect.y += int(self.mass_defined_v * self.velocity[1])
                else:
                    print('=', limits[0] - self.height)
                    self.rect.y = limits[0] - self.height
            else:
                self.rect.y += int(self.mass_defined_v * self.velocity[1])
        self.x = self.rect.x
        self.y = self.rect.y

    def add_chest(self, chest):
        self.chest = chest
