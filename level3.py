import pygame

from captions import Captions
from door_load import Door
from key_load import Key
from level4 import Level4
from level_mask import LevelMask
from load_image import load_image
from moving_platform_load import MovingPlatform
from platform_load import Platform


class Level3(LevelMask):
    def __init__(self, width, height, mus):
        super().__init__(width, height, mus, (50, 456, 240, 360, 240), False, 'training.jpg')
        self.ticks = 0
        self.platforms_list = []

        self.key_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()
        self.moving_platforms_group = pygame.sprite.Group()

        self.draw_platforms()
        self.draw_moving_platforms()
        self.key = Key(self.key_group, self.screen, 1100, 190)
        self.door = Door(self.door_group, self.screen, 24, 340)

        self.is_key = False
        self.execute()

    def draw_platforms(self):
        self.platform = Platform(self.platforms, load_image('platforms/double_grey.png'), self.screen, 500, 500)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

        self.platform = Platform(self.platforms, load_image('platforms/double_grey.png'), self.screen, 900, 300)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

    def draw_moving_platforms(self):
        self.platform = MovingPlatform(self.platforms,
                                       load_image('platforms/spiky_grey.png'), self.screen, 250, 100, 200, 470, 200, 50,
                                       4)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)
        self.moving_platforms_group.add(self.platform)

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            if not self.is_key:
                self.check_key()

            if not self.passed:
                self.check_pass()
            self.check_platform()

            self.all_sprites.draw(self.screen)
            self.door_group.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            if not self.is_key:
                self.key_group.draw(self.screen)
            if self.visible:
                self.mage_group.draw(self.screen)
            else:
                self.ticks += 1
            if self.ticks >= self.FPS * 3 and not self.visible:
                self.visible = True
            self.platforms.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                New = Level3(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True
            if event.key == pygame.K_e and self.passed:
                self.door.open()
            if event.key == pygame.K_RETURN and self.passed and self.mage.x - 50 <= \
                    self.door.x and self.door.is_opened:
                Level4(self.width, self.height, pygame.mixer_music.get_pos())
                self.stop = True

    def check_movement(self):
        pressed = pygame.key.get_pressed()

        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)

    def check_key(self):
        if self.mage.rect.x + 30 >= self.key.rect.x and self.mage.rect.x + 30 <= self.key.rect.x + self.key.w and \
                self.mage.rect.y <= self.key.rect.y:
            self.is_key = True

    def check_pass(self):
        if self.is_key:
            self.passed = True
            self.ticks += 1

    def check_platform(self):
        #if self.mage.x + 10 >= self.platform.rect.x and self.mage.x <= self.platform.w + self.platform.x and \
        #       self.mage.y >= self.platform.rect.y + 100:
        if pygame.sprite.spritecollideany(self.mage, self.moving_platforms_group):
            Level3(self.width, self.height)
            self.stop = True