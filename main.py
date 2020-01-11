import pygame

from main_class import Game
from logo_load import Logo
from mage_image_for_menu import MageMainMenu
from main_menu import MainMenuButton


class TheCageOfMage(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        pygame.mixer_music.stop()
        pygame.mixer_music.load('data/Arti-Fix - Cybernetic Sect.mp3')
        pygame.mixer_music.set_volume(0.049)
        pygame.mixer_music.play(10, 44.0)
        self.is_mouse_button_down = False
        self.buttons_sprites = pygame.sprite.Group()
        self.buttons = []
        self.draw_buttons()
        self.logo_group = pygame.sprite.Group()
        self.logo = Logo(self.logo_group, self.screen, width // 50, -20)
        self.mage_main_menu_group = pygame.sprite.Group()
        self.mage_main_menu = MageMainMenu(self.mage_main_menu_group, self.screen, width // 12, self.height // 4)
        print('не утка')
        self.execute()

    def draw_buttons(self):
        try:
            self.x = self.width // 3 * 2
            self.y = self.height // 4
            texts = ['Continue', 'New game', 'Training']
            for i in range(len(texts)):
                new_btn = MainMenuButton(self.buttons_sprites, self.screen, self.x,
                                         self.y + self.height // 5 * i + 10 * i,
                                         self.is_mouse_button_down, texts[i])
                self.buttons.append(new_btn)
                self.buttons_sprites.add(new_btn)
        except AttributeError:
            pass

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.render()
            self.logo_group.draw(self.screen)
            self.buttons_sprites.draw(self.screen)
            self.mage_main_menu_group.draw(self.screen)
            self.logo_group.update()
            self.buttons_sprites.update()
            self.mage_main_menu_group.update()
            pygame.display.flip()
        self.terminate()

    def terminate(self):
        pygame.quit()

    def handle_event(self, event):
        super().handle_event(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.is_mouse_button_down = True
        else:
            self.is_mouse_button_down = False

    def loop(self):
        super().loop()
        # Здесь движение

    def render(self):
        self.screen.fill(pygame.Color('black'))
        # self.board.render(self.screen)
        # Поле, когда оно появится)))