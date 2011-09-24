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
        if d_y > 0:
            self.image = self.sprites[1]

        new_x = min(max(new_x, 16), 1904)
        new_y = min(max(new_y, 20), 1876)

        collisions = self.get_collisions()
        if len(collisions) > 0:
            for i, collision in enumerate(collisions):
                rect = collision.rect
                if rect.collidepoint(self.rect.midleft):
                    new_x = rect.right - self.screen_position[0]
                elif rect.collidepoint(self.rect.midright):
                    new_x = rect.left - self.screen_position[0] - self.rect.width
                elif rect.collidepoint(self.rect.midbottom):
                    new_y = rect.top - self.screen_position[1] - self.rect.height
                elif rect.collidepoint(self.rect.midtop):
                    new_y = rect.bottom - self.screen_position[1]

        self.set_position(new_x, new_y)

        self.dirty = 1


    def get_collisions(self):
        return bc.utils.sprite.spritecollide(self, self.collision_collection, False)

    def set_position(self, x, y):
        self.position = (x, y)
        self.rect.left = self.screen_position[0] + x
        self.rect.top = self.screen_position[1] + y
