import pygame

from core.classes.chair_sprite import Chair
from core.classes.chest_sprite import Chest
from core.levels.level_mask import LevelMask


class Training(LevelMask):
    def __init__(self, width, height):
        self.chest = None
        self.chest_group = pygame.sprite.Group()
        super().__init__(width, height, 0.0, (50, 456, 240, 360, 240), self.chest_group,
                         'training.jpg')
        self.chair_group = pygame.sprite.Group()

        self.stop = False

        # decorations
        self.chair = Chair(self.chair_group, self.screen, 1080, 580)
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            self.all_sprites.draw(self.screen)
            self.bottom_border.draw(self.screen)
            self.borders.draw(self.screen)
            self.chest_group.draw(self.screen)
            self.chair_group.draw(self.screen)
            self.mage_group.draw(self.screen)

            self.check_movement()
            self.check_movement()
            self.chest_group.update()
            self.chair_group.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        # if event.type == pygame.KEYDOWN:
        #     self.mage.update(event, self.border_b, self.borders)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.chest = Chest(self.chest_group, self.screen, *event.pos)
            self.chest_group.add(self.chest)
            self.all_sprites.add(self.chest)
            self.mage.add_chest(self.chest)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.chest and \
                    abs(self.mage.x + self.mage.image.get_width() - self.chest.x) <= 230 and \
                    abs(self.mage.y + self.mage.image.get_height() - self.chest.y) <= 230:
                self.chest.open()
            if event.key == pygame.K_ESCAPE:
                pygame.mixer_music.load('data/Arti-Fix - Cybernetic Sect.mp3')
                pygame.mixer_music.play(0, 44.0)
                pygame.mixer_music.set_volume(0.049)
                self.stop = True

    def check_movement(self):
        pressed = pygame.key.get_pressed()
        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)
