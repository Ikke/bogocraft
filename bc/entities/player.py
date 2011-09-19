from bc.sprite import Sprite
from bc.utils.alternator import Alternator
from entity import Entity

class Player(Sprite):
    def __init__(self, sprites, screen_position, position):
        final_position = (screen_position[0] + position[0], screen_position[1] + position[1])
        super(Player, self).__init__(sprites[0], final_position)

        self.screen_position = screen_position
        self.position = position

    def move(self, d_x, d_y):
        old_x, old_y = self.position
        self.set_position(old_x - d_x, old_y - d_y)

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect.left = self.screen_position[0] + x
        self.rect.top = self.screen_position[1] + y
