from bc.sprite import Sprite
from bc.utils.alternator import Alternator
from entity import Entity
import bc.utils.sprite


class Player(Sprite):
    def __init__(self, sprites, screen_position, position, collision_collection):
        final_position = (screen_position[0] + position[0], screen_position[1] + position[1])
        super(Player, self).__init__(sprites[0], final_position)

        self.sprites = sprites

        self.screen_position = screen_position
        self.position = position
        self.collision_collection = collision_collection

    def move(self, d_x, d_y):
        old_x, old_y = self.position
        new_x, new_y = old_x - d_x, old_y - d_y

        if d_y < 0:
            self.image = self.sprites[0]
            self.dirty = 1
        if d_y > 0:
            self.image = self.sprites[1]
            self.dirty = 1

        self.set_position(new_x, new_y)

        if self.collides() or not self.in_map():
            self.set_position(old_x, old_y)
        else:
            self.dirty = 1

    def in_map(self):
        x, y = self.position

        return 16 < x < 1904 and 26 < y < 1876

    def collides(self):
        return len(bc.utils.sprite.spritecollide(self, self.collision_collection, False)) > 0

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect.left = self.screen_position[0] + x
        self.rect.top = self.screen_position[1] + y
