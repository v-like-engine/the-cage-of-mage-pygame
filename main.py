import pygame

from main_menu import MainMenuButton


class Game:
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.FPS = 60
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True

    def terminate(self):
        pygame.quit()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.loop()
            self.render()
            pygame.display.flip()
        self.terminate()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        if event.type == pygame.KEYDOWN and event.key in [pygame.KMOD_ALT, pygame.K_F4]:
            self.terminate()

    def loop(self):
        self.clock.tick(self.FPS)

    def render(self):
        pass


class TheCageOfMage(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.is_mouse_button_down = False
        self.buttons_sprites = pygame.sprite.Group()
        self.buttons = []
        self.draw_buttons()
        self.execute()

    def draw_buttons(self):
        try:
            self.x = self.width // 7 * 4
            self.y = self.height // 4
            texts = ['Continue', 'New game', 'Training']
            for i in range(len(texts)):
                new_btn = MainMenuButton(self.buttons_sprites, self.screen, self.x, self.y + self.height // 5 * i,
                                         self.width, self.height,
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
            self.buttons_sprites.update()
            self.render()
            self.buttons_sprites.draw(self.screen)
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


game = TheCageOfMage(1100, 700)
game.execute()