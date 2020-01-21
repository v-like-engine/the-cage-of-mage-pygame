import pygame

from main_class import Game


class Comics(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.ticks = 0
        self.font = pygame.font.Font(self.font, 50)

        self.draw_images()

        self.execute()

    def execute(self):
        pass

    def draw_images(self):
        pass

    def draw_text(self, *text):
        pass