import pygame

from chest_sprite import Chest
from hero_classes import Mage
from level_mask import LevelInRoom
from load_image import load_image
from platform_load import Platform


class Level2(LevelInRoom):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.platforms_list = []
        self.platform = Platform(self.platforms, load_image('platforms/double_brown.png'), self.screen, 400, 600)
        self.platforms_list.append(self.platform)
        self.all_sprites.add(self.platform)
        self.chest_group = pygame.sprite.Group()
        self.chest = Chest(self.chest_group, self.screen, 1050, 450)
        self.chest.image = pygame.transform.flip(self.chest.image, True, False)
        self.chest.opened_image = pygame.transform.flip(self.chest.opened_image, True, False)
        self.all_sprites.add(self.chest)
        self.mage.add_chest(self.chest)
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
            self.chest_group.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.platforms.draw(self.screen)

            self.mage_group.update(event, self.border_b, self.borders)
            self.chest_group.update()
            self.platforms.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o and \
                    abs(self.mage.x + self.mage.image.get_width() - self.chest.x) <= 230 and \
                    abs(self.mage.y + self.mage.image.get_height() - self.chest.y) <= 230:
                self.chest.open()