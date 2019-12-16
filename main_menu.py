from os import path

import pygame

from level_1 import Level1
from training import Training


class MainMenu():
    def __init__(self, width, height, screen, mouse_coords=None, event=None):
        self.screen = screen
        self.mouse_coords = mouse_coords
        self.event = event
        self.width = width
        self.height = height
        self.color = (150, 150, 150)
        self.all_buttons = {}
        self.buttons()

        self.all_sprites = pygame.sprite.Group()
        self.web = 'web.jpg'
        self.web = self.load_image(self.web)

        if self.mouse_coords:
            self.is_mouse_on_button()


    def load_image(self, name):
        fullname = path.join('data', name)
        image = pygame.image.load(fullname).convert()
        return image

    def is_mouse_on_button(self):
        for button in self.all_buttons:
            x = self.all_buttons[button][0]
            y = self.all_buttons[button][1]
            x1 = self.all_buttons[button][2]
            y1 = self.all_buttons[button][3]
            if x <= self.mouse_coords[0] <= x1 and y <= self.mouse_coords[1] <= y1:
                self.highlighting(x, y, x1, y1)
                self.start_game(button)
                break

    def start_game(self, button_text):
        if button_text == 'continue' and self.event == True:
            level = Level1()
            print('кря')
        if button_text == 'new_game' and self.event == True:
            level = Level1()
            print('кря')
        if button_text == 'training' and self.event == True:
            level = Training()
            print('кря')

    def highlighting(self, x, y, x1, y1):
        pygame.draw.rect(self.screen, pygame.Color('white'), (x + 2, y + 2, x1 - x - 2, y1 - y - 2), 1)

    def buttons(self):
        self.font = pygame.font.Font(None, 50)
        self.button_new_game()
        self.button_continue()
        self.button_settings()
        self.button_training()

    def button_location(self):
        self.rect_w = self.width // 5 * 2
        self.rect_h = self.height // 15
        self.rect_x = self.width // 5 * 3

    def button_continue(self):
        self.text = self.font.render("Continue", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                           self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        self.all_buttons['continue'] = (self.rect_x, self.rect_y,
                                        self.rect_x + self.rect_w, self.rect_y + self.rect_h)
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_new_game(self):
        self.text = self.font.render("Start a new game", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        self.all_buttons['new_game'] = (self.rect_x, self.rect_y,
                                        self.rect_x + self.rect_w, self.rect_y + self.rect_h)
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_settings(self):
        self.text = self.font.render("Settings", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h * 2
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                                self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        self.all_buttons['settings'] = (self.rect_x, self.rect_y,
                                        self.rect_x + self.rect_w, self.rect_y + self.rect_h)
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])

    def button_training(self):
        self.text = self.font.render("Training", 1, self.color)
        self.button_location()
        self.rect_y = self.height // 2 + self.rect_h * 3
        self.rect = (self.screen, self.color, (self.rect_x, self.rect_y,
                                               self.rect_w, self.rect_h), 1)
        self.screen.blit(self.text, (self.rect_x + 5, self.rect_y + 5))
        self.all_buttons['training'] = (self.rect_x, self.rect_y,
                                        self.rect_x + self.rect_w, self.rect_y + self.rect_h)
        pygame.draw.rect(self.rect[0], self.rect[1], self.rect[2], self.rect[3])