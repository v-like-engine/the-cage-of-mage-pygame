import pygame

from level_mask import LevelMask
from load_image import load_image


class PrologueLevel(LevelMask):
    def __init__(self, width, height):
        self.cam_coord = 640
        super().__init__(width, height, (self.cam_coord - 160 // 2, 456, 0, 0, 240), False,
                         'hall.jpg', 'hall.jpg')
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
            self.border_b.draw(self.screen)
            self.borders.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.platforms.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def camera_update(self, x):
        if self.bg_frames[-1].rect.x + x > 0:
            x = 0 - self.bg_frames[-1].rect.x
        for el in self.bg_frames:
            el.move_frame(x, 0)
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
        self.mage.update(pressed, self.border_b, self.borders)

