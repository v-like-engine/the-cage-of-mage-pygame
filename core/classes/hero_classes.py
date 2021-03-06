import pygame

from utils.load_image import load_image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, *resize):
        super().__init__()
        self.x = x
        self.y = y
        self.frames = []
        resize = resize or False
        self.cut_sheet(sheet, columns, rows, resize)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
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
    def __init__(self, x, y, hor_v, run_v, vert_v, fps, platforms, cam=False, *box_group):
        self.height = 180
        self.width = 120
        super().__init__(load_image('mage_pictures.png'), 8, 4, x, y, self.width, self.height)
        self.movement_coefficients = [0, 0]
        self.direction = 0
        self.game_fps = fps
        self.frame_fps = 40 / fps
        self.until_frame = 0
        self.walk_velocity = hor_v / fps
        self.current_horisontal_velocity = self.walk_velocity
        self.vertical_velocity = vert_v / fps
        self.run_velocity = run_v / fps
        self.g = 0.2
        self.cam = cam
        self.in_jump = False
        self.platforms = platforms
        if box_group:
            self.box_group = box_group
        self.mask = pygame.mask.from_surface(self.image)
        self.chest = None

    def velocity_change(self, v, r_v, j_v):
        self.walk_velocity = v / self.game_fps
        self.current_horisontal_velocity = self.walk_velocity
        self.vertical_velocity = j_v / self.game_fps
        self.run_velocity = r_v / self.game_fps

    def update(self, pressed=None, *borders):
        dno = borders[0].sprites()[0].coords[1]
        if len(borders) > 2:
            roof = borders[2].sprites()[0].coords[3]
            self.change_coords(2, dno, roof)
        else:
            self.change_coords(2, dno)
        if not pygame.sprite.spritecollideany(self, borders[0]) and \
                not pygame.sprite.spritecollideany(self, self.platforms):
            self.movement_coefficients = self.movement_coefficients[0], self.movement_coefficients[1] + self.g
        else:
            self.movement_coefficients = self.movement_coefficients[0], 0
            self.in_jump = False
        self.direction = -1
        if pressed[pygame.K_LSHIFT]:
            if pressed[pygame.K_LEFT]:
                self.current_horisontal_velocity = self.run_velocity
                self.frame_fps = 60 / self.game_fps
                self.direction = 1
                self.movement_coefficients = -1, self.movement_coefficients[1]
            if pressed[pygame.K_RIGHT]:
                self.current_horisontal_velocity = self.run_velocity
                self.frame_fps = 60 / self.game_fps
                self.direction = 0
                self.movement_coefficients = 1, self.movement_coefficients[1]
        elif pressed[pygame.K_LEFT]:
            self.current_horisontal_velocity = self.walk_velocity
            self.frame_fps = 40 / self.game_fps
            self.direction = 1
            self.movement_coefficients = -1, self.movement_coefficients[1]
        elif pressed[pygame.K_RIGHT]:
            self.current_horisontal_velocity = self.walk_velocity
            self.frame_fps = 40 / self.game_fps
            self.direction = 0
            self.movement_coefficients = 1, self.movement_coefficients[1]
        if pressed[pygame.K_UP] and self.movement_coefficients[1] == 0 and not self.in_jump:
            self.in_jump = True
            self.current_horisontal_velocity = self.walk_velocity
            self.frame_fps = 40 / self.game_fps
            self.direction = -1
            self.movement_coefficients = self.movement_coefficients[0], -5
        if self.direction != -1:
            if self.until_frame > 0.98:
                self.current_frame = (self.current_frame + 1) % (len(self.frames) // 2)
                self.until_frame = 0
            else:
                self.until_frame += self.frame_fps
            frame = self.direction * 16 + self.current_frame
            self.image = self.frames[frame]
            self.change_coords(1)
            if self.chest:
                if pygame.sprite.spritecollideany(self, borders[1]) or \
                        pygame.sprite.collide_mask(self, self.chest):
                    self.movement_coefficients = -self.movement_coefficients[0], self.movement_coefficients[1]
                    self.change_coords(0)
            if pygame.sprite.spritecollideany(self, borders[1]):
                self.movement_coefficients = -self.movement_coefficients[0], self.movement_coefficients[1]
                self.change_coords(1)
        for platform in self.platforms:
            if pygame.sprite.collide_mask(self, platform):
                if platform.rect.x + platform.width > self.x + self.width // 2 > platform.rect.x:
                    if platform.rect.y + platform.height >= self.y + self.height >= platform.rect.y:
                        self.y = platform.rect.y + 2 - self.height
                    else:
                        self.y = platform.rect.y + platform.height + 1
                        self.movement_coefficients = self.movement_coefficients[0], 0
                else:
                    self.movement_coefficients = -self.movement_coefficients[0], self.movement_coefficients[1]
                    self.change_coords(0)
            # self.move(self.x, self.y + 10 / FPS)

    def change_coords(self, x_or_y, *limits):
        if x_or_y in (0, 1):
                self.x += self.current_horisontal_velocity * self.movement_coefficients[0]
        elif x_or_y in (0, 2):
            if limits:
                if limits[0] >= self.rect.y + self.height + self.vertical_velocity * self.movement_coefficients[1]:
                    self.y += int(self.vertical_velocity * self.movement_coefficients[1])
                if len(limits) > 1:
                    if limits[1] <= self.rect.y + self.vertical_velocity * self.movement_coefficients[1]:
                        self.y += int(self.vertical_velocity * self.movement_coefficients[1])
                    else:
                        self.y = limits[1] + 1
                        self.movement_coefficients = self.movement_coefficients[0], 0
                else:
                    self.y = limits[0] - self.height + 2
            else:
                self.rect.y += int(self.vertical_velocity * self.movement_coefficients[1])
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

    def add_chest(self, chest):
        self.chest = chest
