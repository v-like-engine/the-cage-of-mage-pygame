import pygame

from core.classes.background_sprites import Decoration
from core.classes.door_load import Door
from core.levels.level_mask import LevelMask


class CameraLevel(LevelMask):
    def __init__(self, width, height, mus, end=False):
        self.cam_coord = 640
        self.end_level = end
        if end:
            t = ['freedom.png', 'hall_right.jpg']
        else:
            t = ['hall.jpg']
        super().__init__(width, height, mus, (self.cam_coord - 160 // 2, 456, 0, 0, 240), False,
                         *t, 'hall.jpg', 'hall_end.jpg')
        self.main_doors = pygame.sprite.Group()
        self.decor = pygame.sprite.Group()
        if end:
            space = 1280
        else:
            space = 0
        grid0 = Decoration('grid_with_man2.png', 700 - space, 380, 280, 280)
        grid = Decoration('grid.png', 320 - space, 380, 280, 280)
        grid2 = Decoration('grid_with_man.png', -60 - space, 380, 280, 280)
        grid3 = Decoration('grid.png', -440 - space, 380, 280, 280)
        grid4 = Decoration('grid.png', -820 - space, 380, 280, 280)
        grid5 = Decoration('grid_with_man2.png', -1200 - space, 380, 280, 280)
        grid6 = Decoration('grid_with_man.png', -1580 - space, 380, 280, 280)
        grid0.add(self.decor)
        grid.add(self.decor)
        grid2.add(self.decor)
        grid3.add(self.decor)
        grid4.add(self.decor)
        grid5.add(self.decor)
        grid6.add(self.decor)
        if not end:
            coordoor = [-2010, -1856]
        else:
            coordoor = [-3290, -3136]
        door_bg = Decoration('door_frame_fat.png', coordoor[0], 380, 160, 320)
        door_bg.add(self.main_doors)
        self.door = Door(self.main_doors, self.screen, coordoor[1], 380)
        self.door.open()
        self.border_coord = 840
        self.ideal_border_coord = 840
        self.border_space = 120
        self.door_closed = False
        self.ticks_until_level = 20
        self.end = False

    def execute(self):
        while self.running:
            pass
        self.terminate()

    def camera_update(self, x):
        for el in self.bg_frames:
            el.move_frame(x, 0)
        for el in self.decor:
            el.move_frame(x, 0)
        for el in self.main_doors:
            el.move_frame(x, 0)
        if x > 0 or self.border_coord < self.ideal_border_coord:
            self.border_coord -= x
        if self.border_coord + self.border_space < self.ideal_border_coord:
            self.ideal_border_coord = self.border_coord + self.border_space
        self.cam_coord -= x

    def handle_event(self, event):
        super().handle_event(event)

    def check_movement(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LSHIFT]:
            if pressed[pygame.K_LEFT]:
                self.camera_update(360 / self.FPS)
            if pressed[pygame.K_RIGHT]:
                self.camera_update(-360 / self.FPS)
        elif pressed[pygame.K_LEFT]:
            self.camera_update(240 / self.FPS)
        elif pressed[pygame.K_RIGHT]:
            self.camera_update(-240 / self.FPS)
        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)
