from utils.load_image import load_image
from core.classes.simple_sprite import SimpleSprite


class Logo(SimpleSprite):
    def __init__(self, group, screen, x, y):
        super().__init__(group, screen, x, y)
        self.image = load_image('logo.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
