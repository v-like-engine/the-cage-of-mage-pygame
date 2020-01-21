import sys

import pygame

from logo_load import Logo
from main_class import Game


class Captions(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ticks = 0
        self.font = pygame.font.Font(self.font, 50)
        self.logo_group = pygame.sprite.Group()
        logo = Logo(self.logo_group, self.screen, 70, 80)
        logo.rect.x = self.width // 2 - logo.image.get_width() // 2
        logo.rect.y = self.height // 2 - logo.image.get_height() // 2

        self.draw_captions()

        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.screen.fill(pygame.Color('black'))
            if self.ticks <= self.FPS * 5:
                self.draw_captions()
            elif self.ticks <= self.FPS * 10:
                self.draw_other_captions()
            elif self.ticks <= self.FPS * 20:
                self.logo_group.draw(self.screen)
            else:
                return
            self.render()
            self.ticks += 1
            pygame.display.flip()
        self.terminate()

    def draw_captions(self):
        texts = [
            'Realisation:',
            'Denis Mikhailov'
        ]
        for i in range(len(texts)):
            text = texts[i]
            text = self.font.render(text, 1, pygame.Color('white'))
            text_rect = ((self.width // 2 - text.get_width() // 2, self.height // 8 + i * 70))
            self.screen.blit(text, text_rect)

        self.Vlad(2, 60)
        self.simple_text(3, 70, 'Design and graphics')
        self.Vlad(4, 70)
        self.simple_text(5, 70, 'Idea:')
        self.Vlad(6, 70)

    def draw_other_captions(self):
        self.simple_text(0, 60, 'Music:')
        self.simple_text(1, 60, 'Kytami - Sirens')
        self.simple_text(2, 60, 'Arti-Fix - Cybernetic Sect')
        self.simple_text(3, 70, 'Font:')
        self.simple_text(4, 70, 'Chalk_and_Pamor')

    # diff - отступ
    def Vlad(self, k, diff):
        text = 'Vladislav Urzhumov'
        text = self.font.render(text, 1, pygame.Color('white'))
        text_rect = ((self.width // 2 - text.get_width() // 2, self.height // 8 + k * diff))
        self.screen.blit(text, text_rect)

    def simple_text(self, k, diff, text):
        text = self.font.render(text, 1, pygame.Color('white'))
        text_rect = ((self.width // 2 - text.get_width() // 2, self.height // 8 + k * diff))
        self.screen.blit(text, text_rect)
