import random

import pygame

from load_image import load_image


class Cursor:
    def __init__(self, curs, *size):
        arrow_image = load_image('cursors_next_gen.png')
        size = size or False
        self.position = [0, 0]
        self.frames = []
        self.cut_sheet(arrow_image, curs, 40, size)
        self.cursor = random.choice(self.frames)

    def change_color(self):
        self.cursor = random.choice(self.frames)

    def cut_sheet(self, sheet, columns, height, size=(20, 20)):
        width = 240 // columns
        for i in range(columns):
            x = width * i
            y = 0
            print(x, y, width, height)
            image = sheet.subsurface(x, y, width, height)
            image = pygame.transform.scale(image, size)
            self.frames.append(image)
