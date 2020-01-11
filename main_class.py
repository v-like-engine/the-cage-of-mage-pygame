import pygame


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
            self.terminate()
        if event.type == pygame.KEYDOWN and pygame.key.get_mods() & pygame.KMOD_ALT:
            if event.key == pygame.K_F4:
                self.running = False
                self.terminate()
        # if event.type == pygame.MOUSEMOTION:
        #     cursor_pos = event.pos

    def loop(self):
        self.clock.tick(self.FPS)

    def render(self):
        pass