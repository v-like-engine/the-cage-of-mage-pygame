import pygame

from chest_sprite import Chest
from key_load import Key
from level_mask import LevelMask
from load_image import load_image
from moving_platform_load import MovingPlatform
from platform_load import Platform


class Level3(LevelMask):
    def __init__(self, width, height):
        super().__init__(width, height, (50, 456, 240, 360, 240), False, 'training.jpg')
        self.ticks = 0
        self.platforms_list = []

        self.key_group = pygame.sprite.Group()

        self.draw_platforms()
        self.draw_moving_platforms()
        self.key = Key(self.key_group, self.screen, 1100, 190)
        self.is_key = False
        self.execute()

    def draw_platforms(self):
        self.platform = Platform(self.platforms, load_image('platforms/double_brown.png'), self.screen, 400, 500)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

        self.platform = Platform(self.platforms, load_image('platforms/triple_brown.png'), self.screen, 600, 300)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

    def draw_moving_platforms(self):
        self.platform = MovingPlatform(self.platforms, load_image('platforms/simple_grey.png'), self.screen, 200, 100)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            if not self.is_key:
                self.check_key()

            self.all_sprites.draw(self.screen)
            self.border_b.draw(self.screen)
            self.borders.draw(self.screen)
            if not self.is_key:
                self.key_group.draw(self.screen)
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

    def check_key(self):
        if self.mage.rect.x + 30 >= self.key.rect.x and self.mage.rect.x + 30 <= self.key.rect.x + self.key.w and \
                self.mage.rect.y <= self.key.rect.y:
            self.is_key = True
