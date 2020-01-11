import sys

import pygame

from cursor_class import Cursor


class Game:
    def __init__(self, width, height):
        self.size = self.width, self.height = width, height
        self.FPS = 60
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.clock = pygame.time.Clock()
        self.running = True
        pygame.mouse.set_visible(False)
        self.cursor = Cursor(6, 120, 120)

    def terminate(self):
        pygame.quit()
        sys.exit(0)

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
        if event.type == pygame.MOUSEMOTION:
            self.cursor.position = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.cursor.change_color()

    def loop(self):
        self.clock.tick(self.FPS)

    def render(self):
        self.screen.fill(pygame.Color('black'))
        if pygame.mouse.get_focused():
            self.screen.blit(self.cursor.cursor, self.cursor.position)
