import pygame

from chest_sprite import Chest
from door_load import Door
from level3 import Level3
from level_mask import LevelMask
from load_image import load_image
from platform_load import Platform


class Level2(LevelMask):
    def __init__(self, width, height):
        super().__init__(width, height, (50, 456, 240, 360, 240), False, 'training.jpg')
        self.platforms_list = []
        self.platform = Platform(self.platforms, load_image('platforms/double_brown.png'), self.screen, 400, 600)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)

        self.chest_group = pygame.sprite.Group()
        self.door_group = pygame.sprite.Group()

        self.chest = Chest(self.chest_group, self.screen, 1050, 480)
        self.chest.image = pygame.transform.flip(self.chest.image, True, False)
        self.chest.opened_image = pygame.transform.flip(self.chest.opened_image, True, False)
        self.all_sprites.add(self.chest)
        self.mage.add_chest(self.chest)
        self.door = Door(self.door_group, self.screen, 20, 340)
        self.passed = False
        self.ticks = 0
        self.door_opened = False
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()
            self.check_pass()

            if self.passed:
                self.ticks += 1

            self.all_sprites.draw(self.screen)
            self.door_group.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            self.chest_group.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.platforms.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.chest_group.update()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o and \
                    abs(self.mage.x + self.mage.image.get_width() - self.chest.x) <= 230 and \
                    abs(self.mage.y + self.mage.image.get_height() - self.chest.y) <= 230:
                self.chest.open()
            if event.key == pygame.K_r:
                New = Level2(self.width, self.height)
                self.stop = True
            if event.key == pygame.K_RETURN and self.passed and self.ticks >= self.FPS and self.mage.x - 50 <= \
                    self.door.x:
                Level3(self.width, self.height)
                self.stop = True

    def check_movement(self):
        pressed = pygame.key.get_pressed()
        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)

    def check_pass(self):
        if self.chest.image == self.chest.opened_image and not self.door_opened:
            self.door.open()
            self.door_opened = True
            self.passed = True
            self.ticks += 1
