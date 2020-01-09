from os import path

import pygame

from new_training import Training


class MainMenuButton(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y, event, text):
        super().__init__(group)
        self.group = group
        self.screen = screen
        self.event = event
        self.x = x
        self.y = y
        self.stock = self.load_image('butt_n.png')
        self.highlighting_image = self.load_image('target.png')
        self.image = self.stock
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.color = pygame.Color('grey')
        self.text = text

        font = pygame.font.Font(None, 50)
        text = font.render(text, 1, self.color)
        text_rect = ((self.rect.width - text.get_width()) // 2,
                     (self.rect.height - text.get_height()) // 2)
        self.stock.blit(text, text_rect)
        self.highlighting_image.blit(text, text_rect)

    def load_image(self, name, colorkey=None):
        fullname = path.join('data', name)
        image = pygame.image.load(fullname).convert_alpha()
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    def update(self):
        if self.rect.collidepoint(*pygame.mouse.get_pos()):
            self.image = self.highlighting_image
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(self.text)
                    if self.text == 'Training':
                        Training(1280, 720)
                        return
        else:
            self.image = self.stock
