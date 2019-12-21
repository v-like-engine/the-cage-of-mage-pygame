from os import path

import pygame


class MainMenuButton(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y, width, height, event, text):
        super().__init__(group)
        self.group = group
        self.screen = screen
        self.event = event
        self.width = width
        self.height = height
        self.w = self.width // 5 * 2
        self.h = self.height // 15
        self.x = x
        self.y = y
        self.image = pygame.Surface([self.w, self.h])
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.color = pygame.Color('grey')
        pygame.draw.rect(self.image, self.color, (0, 0, self.w, self.h), 1)

        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render(text, 1, self.color)
        self.image.blit(self.text, (self.w // 2 - self.text.get_width() // 2,
                                    self.h // 2 - self.text.get_height() // 2))

        self.all_sprites = pygame.sprite.Group()
        self.web = 'web.jpg'
        self.web = self.load_image(self.web)


    def load_image(self, name):
        fullname = path.join('data', name)
        image = pygame.image.load(fullname).convert()
        return image
'''
    def highlighting(self):
        light = pygame.Rect(2, 2, self.w - 2, self.h - 2)
        pygame.draw.rect(self.light_image, pygame.Color('white'), light, 1)
'''
