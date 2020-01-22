import pygame

from background_sprites import Decoration
from door_load import Door
from effects import ScreenEffect
from level2 import Level2
from level_mask import LevelMask


class PrologueLevel(LevelMask):
    def __init__(self, width, height, mus, end=False):
        self.cam_coord = 640
        self.end_level = end
        if end:
            t = ['freedom.png', 'hall_right.jpg']
        else:
            t = ['hall.jpg']
        print(*t)
        super().__init__(width, height, mus, (self.cam_coord - 160 // 2, 456, 0, 0, 240), False,
                         *t, 'hall.jpg', 'hall_end.jpg')
        if not end:
            self.tma_effect = pygame.sprite.Group()
        self.decor = pygame.sprite.Group()
        if end:
            space = -1280
        else:
            space = 0
        grid0 = Decoration('grid_with_man2.png', 700 + space, 380, 280, 280)
        grid = Decoration('grid.png', 320 + space, 380, 280, 280)
        grid2 = Decoration('grid_with_man.png', -60 + space, 380, 280, 280)
        grid3 = Decoration('grid.png', -440 + space, 380, 280, 280)
        grid4 = Decoration('grid.png', -820 + space, 380, 280, 280)
        grid5 = Decoration('grid_with_man2.png', -1200 + space, 380, 280, 280)
        grid6 = Decoration('grid_with_man.png', -1580 + space, 380, 280, 280)
        grid0.add(self.decor)
        grid.add(self.decor)
        grid2.add(self.decor)
        grid3.add(self.decor)
        grid4.add(self.decor)
        grid5.add(self.decor)
        grid6.add(self.decor)
        self.main_doors = pygame.sprite.Group()
        if not end:
            coordoor = [-2020, -1866]
        else:
            coordoor = [-3300, -3146]
        door_bg = Decoration('door_frame_fat.png', coordoor[0], 380, 160, 320)
        door_bg.add(self.main_doors)
        self.door = Door(self.main_doors, self.screen, coordoor[1], 380)
        self.door.open()
        self.border_coord = 840
        self.ideal_border_coord = 840
        self.border_space = 120
        if not end:
            tma = ScreenEffect('tma.png', 0, 0)
            tma.add(self.tma_effect)
        self.door_closed = False
        self.ticks_until_level = 20
        self.end = False
        if not end:
            self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()
            self.screen.fill(pygame.Color('#383636'))

            self.all_sprites.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            self.backgrounds.draw(self.screen)
            self.decor.draw(self.screen)
            self.platforms.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.main_doors.draw(self.screen)
            if not self.end_level:
                self.tma_effect.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            if self.ticks_until_level <= 0:
                New = Level2(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True
            elif self.end:
                self.ticks_until_level -= 1
            self.render()
        self.terminate()

    def camera_update(self, x):
        if self.cam_coord + self.mage.width // 2 < self.border_coord or x > 0 or\
                self.border_coord < self.ideal_border_coord:
            if self.bg_frames[-1].rect.x + x > 50:
                x = 50 - self.bg_frames[-1].rect.x
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
            if self.cam_coord <= -1940:
                self.end_of_the_prologue()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = PrologueLevel(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True

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

    def end_of_the_prologue(self):
        if not self.door_closed:
            self.door.open()
            self.door_closed = True
        self.border_coord = self.cam_coord + self.mage.width // 2
        self.ideal_border_coord = self.cam_coord + self.mage.width // 2
        self.border_space = 0
        self.mage.velocity_change(0, 0, 0)
        self.end = True
