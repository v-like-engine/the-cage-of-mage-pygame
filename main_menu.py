import pygame

class MainMenu():
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.color = (150, 150, 150)
        self.buttons()

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