import pygame

from background_sprites import Background, Border
from hero_classes import Mage
from main_class import Game


class LevelMask(Game):
    def __init__(self, width, height, mage_prefs, chests, background_file, *camera_frames):
        super().__init__(width, height)
        pygame.mixer_music.load('data/Kytami-Sirens.mp3')
        pygame.mixer_music.play(100, 0.0)
        pygame.mixer_music.set_volume(0.049)

        self.all_sprites = pygame.sprite.Group()
        self.mage_group = pygame.sprite.Group()
        self.bottom_border = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.border_roof = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.FPS = self.FPS
        self.screen = self.screen
        self.mage = Mage(*mage_prefs, self.FPS, self.platforms, chests)
        self.mage.add(self.all_sprites)
        self.mage.add(self.mage_group)

        training_background = Background(background_file, 0, 0)
        training_background.add(self.all_sprites)
        if camera_frames:
            self.bg_frames = [training_background]
            x_frame = 0
            for el in camera_frames:
                frame = Background(el, x_frame, 0)
                frame_width = -frame.image.get_size()[0]
                frame.move_frame(frame_width, 0)
                x_frame += frame_width
                self.bg_frames.append(frame)
                frame.add(self.backgrounds)
        border_bottom = Border(1280, 64, 0, 692)
        border_bottom.add(self.bottom_border)
        border_top = Border(1280, 32, 0, 0)
        border_top.add(self.border_roof)
        border_left = Border(32, 720, 0, 0)
        border_right = Border(32, 720, 1248, 0)
        border_left.add(self.borders)
        border_right.add(self.borders)

        self.stop = False
        self.ticks = 0
        self.passed = False

    # def execute(self):
    #     while self.running:
    #         for event in pygame.event.get():
    #             self.handle_event(event)
    #         if self.stop:
    #             return
    #         self.loop()
    #
    #         self.all_sprites.draw(self.screen)
    #         self.border_b.draw(self.screen)
    #         self.borders.draw(self.screen)
    #         self.mage_group.draw(self.screen)
    #
    #         self.mage_group.update(event, 10, self.border_b, self.borders)
    #
    #         pygame.display.flip()
    #         self.clock.tick(self.FPS)
    #         self.ticks += 1
    #         self.render()
    #     self.terminate()

    def handle_event(self, event):
        super().handle_event(event)
        # self.check_movement()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.mixer_music.load('data/Arti-Fix - Cybernetic Sect.mp3')
                pygame.mixer_music.play(0, 44.0)
                pygame.mixer_music.set_volume(0.049)
                self.stop = True

    def check_movement(self):
        pressed = pygame.key.get_pressed()
        self.mage.update(pressed, self.bottom_border, self.borders, self.border_roof)
