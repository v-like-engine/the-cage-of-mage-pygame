import pygame

from Chair import Chair
from background_sprites import Background, Border
from chest import Chest
from hero_classes import Mage
from main import Game


class Training(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        pygame.mixer_music.load('data/Kytami-Sirens.mp3')
        pygame.mixer_music.play()
        pygame.mixer_music.set_volume(pygame.mixer_music.get_volume() * 0.02)
        self.ticks = 0
        self.chest = None

        self.all_sprites = pygame.sprite.Group()
        self.mage_group = pygame.sprite.Group()
        self.border_b = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.chest_group = pygame.sprite.Group()
        self.chair_group = pygame.sprite.Group()

        training_background = Background('training.jpg', 0, -30)
        training_background.add(self.all_sprites)
        border_bottom = Border(1280, 64, 0, 656)
        border_bottom.add(self.border_b)
        border_left = Border(32, 720, 0, 0)
        border_right = Border(32, 720, 1248, 0)
        border_left.add(self.borders)
        border_right.add(self.borders)
        self.mage = Mage(50, 0, self.FPS, self.chest_group)
        self.mage.add(self.all_sprites)
        self.mage.add(self.mage_group)

        # decorations
        self.chair = Chair(self.chair_group, self.screen, 200, 200)

        pygame.key.set_repeat(10)
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.render()

            self.all_sprites.draw(self.screen)
            self.border_b.draw(self.screen)
            self.borders.draw(self.screen)
            self.chest_group.draw(self.screen)
            self.mage_group.draw(self.screen)
            self.chair_group.draw(self.screen)

            self.mage_group.update(event, 10, self.border_b, self.borders)
            self.chest_group.update()
            self.chair_group.update()

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.KEYDOWN:
            self.mage.update(event, 10, self.border_b, self.borders)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.chest = Chest(self.chest_group, self.screen, *event.pos)
            self.chest_group.add(self.chest)
            self.all_sprites.add(self.chest)
            self.mage.add_chest(self.chest)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o and self.chest and \
                    abs(self.mage.x + self.mage.image.get_width() - self.chest.x) <= 230 and \
                    abs(self.mage.y + self.mage.image.get_height() - self.chest.y) <= 230:
                self.chest.open()

    def render(self):
        self.screen.fill(pygame.Color('#383636'))