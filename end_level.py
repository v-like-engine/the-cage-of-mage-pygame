import pygame

from background_sprites import Decoration
from door_load import Door
from effects import ScreenEffect
from level2 import Level2
from main import TheCageOfMage
from prologue_level import PrologueLevel


class EndLevel(PrologueLevel):
    def __init__(self, width, height):
        self.cam_coord = 640
        super().__init__(width, height, True)
        self.camera_move()
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
            self.main_door.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            if self.ticks_until_level <= 0:
                New = TheCageOfMage(self.width, self.height)
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
            for el in self.main_door:
                el.move_frame(x, 0)
            if x > 0 or self.border_coord < self.ideal_border_coord:
                self.border_coord -= x
            if self.border_coord + self.border_space < self.ideal_border_coord:
                self.ideal_border_coord = self.border_coord + self.border_space
            self.cam_coord -= x

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = EndLevel(self.width, self.height)
                self.stop = True

    def camera_move(self, x):
        for el in self.bg_frames:
            el.move_frame(x, 0)
        for el in self.decor:
            el.move_frame(x, 0)
        for el in self.main_door:
            el.move_frame(x, 0)
        if x > 0 or self.border_coord < self.ideal_border_coord:
            self.border_coord -= x
        if self.border_coord + self.border_space < self.ideal_border_coord:
            self.ideal_border_coord = self.border_coord + self.border_space
        self.cam_coord -= x
        if self.cam_coord <= -1940:
            self.end_of_the_prologue()

    def check_movement(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LSHIFT]:
            if pressed[pygame.K_LEFT]:
                self.camera_update(1660 / self.FPS)
            if pressed[pygame.K_RIGHT]:
                self.camera_update(-1660 / self.FPS)
        elif pressed[pygame.K_LEFT]:
            self.camera_update(240 / self.FPS)
        elif pressed[pygame.K_RIGHT]:
            self.camera_update(-240 / self.FPS)
        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)

    def end_of_the_end(self):
        pass

    def close_door(self):
        pass
