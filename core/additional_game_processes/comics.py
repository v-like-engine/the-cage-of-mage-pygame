import pygame

from core.classes.background_sprites import Decoration
from core.menu.main import TheCageOfMage
from core.menu.main_class import Game
from utils.text_import_from_file import load_text


class Comics(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ticks = 0
        self.font = pygame.font.Font(self.font, 30)
        text_strs = load_text('data/mage_comics.txt')
        self.text = []
        self.stop = False
        while '\n' in text_strs:
            k = text_strs.index('\n')
            self.text.append(text_strs[:k])
            text_strs = text_strs[k + 1:]
        self.text.append(text_strs)
        self.number_of_text = 0
        dragon = Decoration('comics/dragon_comics.png', 280, 40, 720, 540)
        self.dragon_group = pygame.sprite.Group()
        dragon.add(self.dragon_group)
        mage_escape = Decoration('comics/mage_escape_comics.png', 280, 40, 720, 540)
        self.mage_escape_group = pygame.sprite.Group()
        mage_escape.add(self.mage_escape_group)
        throne = Decoration('comics/throne_comics.png', 280, 40, 720, 540)
        self.throne_group = pygame.sprite.Group()
        throne.add(self.throne_group)
        self.comics_image_group = None

        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.screen.fill(pygame.Color('black'))
            self.number_of_text = int(self.ticks // (self.FPS * (61.4 / len(self.text))))
            if self.number_of_text > len(self.text) - 1:
                New = TheCageOfMage(self.width, self.height)
                return
            if self.ticks == self.FPS * 4:
                pygame.mixer_music.stop()
                pygame.mixer_music.load('data/Arti-Fix - Cybernetic Sect.mp3')
                pygame.mixer_music.set_volume(0.049)
                pygame.mixer_music.play(10, 0.0)
            if self.ticks == self.FPS * 22:
                pygame.mixer_music.stop()
                pygame.mixer_music.load('data/Arti-Fix - Cybernetic Sect.mp3')
                pygame.mixer_music.set_volume(0.049)
                pygame.mixer_music.play(10, 0.0)
            if self.ticks <= self.FPS * 12:
                self.comics_image_group = None
            elif self.ticks <= self.FPS * 29:
                self.comics_image_group = self.dragon_group
            elif self.ticks <= self.FPS * 41:
                self.comics_image_group = self.mage_escape_group
            elif self.ticks <= self.FPS * 54:
                self.comics_image_group = self.throne_group
            elif self.ticks <= self.FPS * 62:
                self.comics_image_group = None
            else:
                return
            self.draw_images()
            self.draw_text()
            self.render()
            self.ticks += 1
            pygame.display.flip()
            if self.stop:
                TheCageOfMage(self.width, self.height)
                return
        self.terminate()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop = True

    def draw_images(self):
        if self.comics_image_group:
            self.comics_image_group.draw(self.screen)

    def draw_text(self):
        for i in range(len(self.text[self.number_of_text])):
            for i in range(len(self.text[self.number_of_text])):
                text_draw = self.font.render(self.text[self.number_of_text][i], 1, pygame.Color('white'))
                text_rect = (self.width // 2 - text_draw.get_width() // 2,
                             600 + i * 40)
                self.screen.blit(text_draw, text_rect)
