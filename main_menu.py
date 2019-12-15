from os import path

import pygame

class MainMenu():
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = (150, 150, 150)
        self.buttons()

        self.all_sprites = pygame.sprite.Group()
        self.web = 'web.jpg'
        self.web = self.load_image(self.web)
        for i in range(10):
            self.web_sprite = pygame.sprite.Sprite()
            self.web_sprite.image = self.web
            self.web_sprite.rect = self.web_sprite.image.get_rect()
            self.web_sprite.rect.x = -100 + 236 * i
            self.web_sprite.rect.y = -50
            self.all_sprites.add(self.web_sprite)

        for i in range(10):
            self.web_sprite = pygame.sprite.Sprite()
            self.web_sprite.image = self.web
            self.web_sprite.rect = self.web_sprite.image.get_rect()
            self.web_sprite.rect.x = -100
            self.web_sprite.rect.y = -50 + 208 * i
            self.all_sprites.add(self.web_sprite)

        for i in range(10):
            self.web_sprite = pygame.sprite.Sprite()
            self.web_sprite.image = self.web
            self.web_sprite.rect = self.web_sprite.image.get_rect()
            self.web_sprite.rect.x = -100 + 236 * i
            self.web_sprite.rect.y = self.height - 100
            self.all_sprites.add(self.web_sprite)

        for i in range(10):
            self.web_sprite = pygame.sprite.Sprite()
            self.web_sprite.image = self.web
            self.web_sprite.rect = self.web_sprite.image.get_rect()
            self.web_sprite.rect.x = -100 - 236 * i
            self.web_sprite.rect.y = self.height - 100
            self.all_sprites.add(self.web_sprite)


    def load_image(self, name):
        fullname = path.join('data', name)
        image = pygame.image.load(fullname).convert()
        return image

    def buttons(self):
        self.font = pygame.font.Font(None, 50)
        self.button_new_game()
        self.button_continue()
        self.button_settings()
        self.button_levels()

    def button_location(self):
        self.rect_w = self.width // 1.5
        self.rect_h = self.height // 15
        self.rect_x = self.width // 6

    def button_continue(self):
        self.text = self.font.render("Continue", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                           self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_new_game(self):
        self.text = self.font.render("Start a new game", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_settings(self):
        self.text = self.font.render("Settings", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h * 2
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_levels(self):
        self.text = self.font.render("Levels", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h * 3
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                               self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])