import pygame

from background_sprites import Decoration, Border
from effects import ScreenEffect
from level_mask import LevelMask


class PrologueLevel(LevelMask):
    def __init__(self, width, height):
        self.cam_coord = 640
        super().__init__(width, height, (self.cam_coord - 160 // 2, 456, 0, 0, 240), False,
                         'hall.jpg', 'hall.jpg', 'hall_end.jpg')
        self.tma_effect = pygame.sprite.Group()
        self.decor = pygame.sprite.Group()
        grid0 = Decoration('grid_with_man2.png', 700, 380, 280, 280)
        grid = Decoration('grid.png', 320, 380, 280, 280)
        grid2 = Decoration('grid_with_man.png', -60, 380, 280, 280)
        grid3 = Decoration('grid.png', -440, 380, 280, 280)
        grid4 = Decoration('grid.png', -820, 380, 280, 280)
        grid5 = Decoration('grid_with_man2.png', -1200, 380, 280, 280)
        grid6 = Decoration('grid_with_man.png', -1580, 380, 280, 280)
        grid0.add(self.decor)
        grid.add(self.decor)
        grid2.add(self.decor)
        grid3.add(self.decor)
        grid4.add(self.decor)
        grid5.add(self.decor)
        grid6.add(self.decor)
        self.border_coord = 840
        self.ideal_border_coord = 840
        self.border_space = 120
        tma = ScreenEffect('tma.png', 0, 0)
        tma.add(self.tma_effect)
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
            self.tma_effect.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def camera_update(self, x):
        if self.cam_coord + self.mage.width // 2 < self.border_coord or x > 0 or\
                self.border_coord < self.ideal_border_coord:
            if self.bg_frames[-1].rect.x + x > 0:
                x = 0 - self.bg_frames[-1].rect.x
            for el in self.bg_frames:
                el.move_frame(x, 0)
            for el in self.decor:
                el.move_frame(x, 0)
            if x > 0 or self.border_coord < self.ideal_border_coord:
                self.border_coord -= x
                print(self.border_coord, self.ideal_border_coord)
            if self.border_coord + self.border_space < self.ideal_border_coord:
                self.ideal_border_coord = self.border_coord + self.border_space
            self.cam_coord -= x

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = PrologueLevel(self.width, self.height)
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
