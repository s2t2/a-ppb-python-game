from os import path
from ppb import GameEngine, BaseScene
from pygame import image
from pygame.sprite import DirtySprite
from pygame import mouse

class Player(DirtySprite):

    def __init__(self, scene):
        super().__init__(scene.groups["player"])
        self.image = image.load(path.join(path.dirname(__file__), "img/zombie_hold1.png"))
        self.rect = self.image.get_rect()
        self.scene = scene

    #def update(self, time_delta):
    #    self.rect.center = mouse.get_pos()
    #    self.dirty = True

    def update(self, *args):
        mouse_x, mouse_y = mouse.get_pos()
        diff_x = max(min(mouse_x - self.rect.centerx, 5), -5)
        diff_y = max(min(mouse_y - self.rect.centery, 5), -5)
        self.rect.centerx += diff_x
        self.rect.centery += diff_y
        if diff_x or diff_y:
            self.dirty = True

class Game(BaseScene):

    def __init__(self, engine, background_color=(90, 55, 100), **kwargs):
        super().__init__(engine=engine, background_color=background_color, **kwargs)
        Player(self)

def main():
    with GameEngine(Game, resolution=(400, 600)) as engine:
        engine.run()

if __name__ == "__main__":
    main()
