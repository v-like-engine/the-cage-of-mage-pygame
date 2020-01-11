import pygame

from level_mask import LevelInRoom


class NewLevel(LevelInRoom):
    def __init__(self, width, height):
        super().__init__(width, height)
        print('я утка')
        self.execute()

    def execute(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.stop:
                return
            self.loop()

            self.all_sprites.draw(self.screen)
            self.border_b.draw(self.screen)
            self.borders.draw(self.screen)
            self.mage_group.draw(self.screen)

            self.mage_group.update(event, 10, self.border_b, self.borders)

            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.ticks += 1
            self.render()
        self.terminate()

    def handle_event(self, event):
        super().handle_event(event)