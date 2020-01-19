import pygame

from chest_sprite import Chest
from level_mask import LevelMask
from load_image import load_image
from moving_platform_load import MovingPlatform
from platform_load import Platform


class Level3(LevelMask):
    def __init__(self, width, height):
        super().__init__(width, height, (50, 456, 240, 360, 240), False, 'training.jpg')
        self.platforms_list = []
        self.platform = Platform(self.platforms, load_image('platforms/double_brown.png'), self.screen, 400, 500)
        self.platforms_list.append(self.platform)
        self.platform = MovingPlatform(self.platforms, load_image('platforms/double_brown.png'), self.screen, 300, 100)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

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

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = Level3(self.width, self.height)
                self.stop = True

    def check_movement(self):
        pressed = pygame.key.get_pressed()

        self.mage.update(pressed, self.border_b, self.borders)
