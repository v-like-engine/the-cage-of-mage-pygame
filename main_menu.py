from os import path

import pygame


class MainMenuButton(pygame.sprite.Sprite):
    def __init__(self, group, screen, x, y, width, height, event, text, pos):
        super().__init__(group)
        self.pos = pos
        self.group = group
        self.screen = screen
        self.event = event
        self.width = width
        self.height = height
        self.w = self.width // 5 * 2
        self.h = self.height // 15
        self.x = x
        self.y = y
        self.stock = self.load_image('button.png')
        self.highlighting_image = self.load_image('targeted.png')
        self.image = self.stock
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.w = self.w
        self.rect.h = self.h
        self.color = pygame.Color('grey')

        self.font = pygame.font.Font(None, 50)
        self.text = self.font.render(text, 1, self.color)
        self.image.blit(self.text, (self.rect.w // 2 - 20 - self.text.get_width() // 2,
                                    self.rect.h // 3 * 4 - self.text.get_height() // 2))

        self.all_sprites = pygame.sprite.Group()
        self.web = 'web.jpg'
        self.web = self.load_image(self.web)

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
        self.pos = pygame.mouse.get_pos()
        mouse_x = self.pos[0]
        mouse_y = self.pos[1]
        if self.rect.x <= mouse_x <= self.rect.x + self.width and self.rect.y <= mouse_y <= self.rect.y:
            self.image = self.highlighting_image
        else:
            self.image = self.stock
