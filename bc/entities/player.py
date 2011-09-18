from bc.utils.alternator import Alternator
from entity import Entity

class Player(Entity):
    def __init__(self, screen_size, sprites, game_map):

        size = sprites[0].get_size()
        position = (screen_size[0] / 2 - size[0] / 2, screen_size[1] / 2 - size[1] / 2)
        super(Player, self).__init__(position)

        self.sprites = Alternator(*sprites)
        self.tick_count = 0
        self.map = game_map

    def tick(self):
        if not self.tick_count:
            self.current_sprite = self.sprites.get()
        self.tick_count = (self.tick_count + 1) % 30


    def move(self, x, y):
        self.map.move_view(-x, -y)
