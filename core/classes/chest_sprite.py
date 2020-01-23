from utils.load_image import load_image
from core.classes.simple_sprite import SimpleSprite


class Chest(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        self.stock_image = load_image('chest.png')
        self.opened_image = load_image('chest_opened.png')
        self.image = self.stock_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def open(self):
        self.image = self.opened_image
