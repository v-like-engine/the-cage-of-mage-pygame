import pygame

from core.classes.background_sprites import Decoration
from core.i.captions import Captions
from core.levels.prologue_level import PrologueLevel


class EndLevel(PrologueLevel):
    def __init__(self, width, height, mus):
        self.save('EndLevel')
        self.cam_coord = 640
        super().__init__(width, height, mus, True)
        backdoor = Decoration('door_frame_high.png', -190, 220)
        backdoor.add(self.main_doors)
        self.moved = False
        self.last_mage = pygame.sprite.Group()
        self.new_mage = Decoration('mage_image.png', 560, 416, 210, 280)
        self.new_mage.add(self.last_mage)
        self.ticks_until_level = self.FPS * 3
        self.end_of_the_end = False
        self.redraw = False
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
            if not self.end_of_the_end:
                self.mage_group.draw(self.screen)
            else:
                self.last_mage.draw(self.screen)
            self.main_doors.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()
            if not self.moved:
                self.camera_move(3860)
                self.moved = True

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            if self.ticks_until_level <= 0:
                print(self.ticks, self.ticks_until_level)
                New = Captions(self.width, self.height)
                self.stop = True
            elif self.end_of_the_end:
                self.ticks_until_level -= 1
            self.render()
        self.terminate()

    def camera_update(self, x):
        if self.cam_coord < 640:
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
        else:
            self.end_movement()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = EndLevel(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True

    def restart(self):
        EndLevel(1280, 720, 0.0)
        self.stop = True

    def camera_move(self, x):
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

    def end_movement(self):
        self.end_of_the_end = True
