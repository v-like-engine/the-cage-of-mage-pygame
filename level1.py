import pygame

from captions import Captions
from door_load import Door
from key_load import Key
from level2 import Level2
from level4 import Level4
from level_mask import LevelMask
from load_image import load_image
from moving_platform_load import MovingPlatform
from platform_load import Platform


class Level1(LevelMask):
    def __init__(self, width, height, mus):
        super().__init__(width, height, mus, (50, 456, 240, 360, 240), False, 'training.jpg')
        self.ticks = 0
        self.platforms_list = []

        self.door_group = pygame.sprite.Group()
        self.key_group = pygame.sprite.Group()
        self.opened_door = False

        self.door = Door(self.door_group, self.screen, 1222, 340)
        self.door.simple_image = pygame.transform.flip(self.door.simple_image, True, False)
        self.door.opened = pygame.transform.flip(self.door.opened, True, False)

        self.key = Key(self.key_group, self.screen, 500, 600)
        self.is_key = False

        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            if not self.passed:
                self.check_pass()

            self.all_sprites.draw(self.screen)
            self.door_group.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)

            if not self.is_key:
                self.check_key()
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
                self.restart()
            if event.key == pygame.K_e and self.passed and not self.opened_door:
                self.door.open()
                self.opened_door = True
                self.door.rect.x -= self.door.image.get_width()
            if event.key == pygame.K_RETURN and self.passed and self.mage.x - 50 <= \
                    self.door.x and self.door.is_opened:
                Level2(self.width, self.height)
                self.stop = True

    def restart(self):
        New = Level1(self.width, self.height)
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