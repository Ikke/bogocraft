import logging
from bc import graphics, sprite
from bc.gameobjects.tree import Tree
from bc.gameobjects.log import Log

logger = logging.getLogger('map')

class Map(object):
    def __init__(self, sprite_group, size = (60, 60), tile_size = (32, 32)):

        self.size = size
        self.tile_size = tile_size
        self.sprites = sprite_group

        self.view = (0, 0, self.size[0] * self.tile_size[0], self.size[1] * self.tile_size[1])
        self.entity_added_handlers = []

    def move_view(self, x, y):
        self.view = (max(min(self.view[0] + x, 1920), 0), max(min(self.view[1] + y, 1920), 0), self.view[2], self.view[3])
        #print self.view


    def load_map(self):
        for k in range(0, self.size[0] * self.size[1]):
            spr = sprite.Sprite(graphics.grass, (400 + k % self.size[0] * self.tile_size[0],
                                                 300 + k // self.size[1] * self.tile_size[1]))
            self.add_entity(spr, layer=0)


        for k in range(100):
            spr = sprite.Sprite(graphics.forrest, (592 + k % 10 * self.tile_size[0],
                                                   620 + k // 10 * self.tile_size[1]))
            self.add_entity(spr, layer=0)

        sprites = [
            Tree((630, 687)),
            Tree((750, 710)),
            Tree((830, 790)),
            Tree((630, 845)),
            Tree((915, 841)),
            Tree((601, 638)),
            Tree((787, 957)),
            Tree((840, 681)),
            Tree((678, 900)),
            Tree((716, 834)),
            Log((800, 800))
        ]
        for entity in sprites:
            self.add_entity(entity, 5)

        #self.collision_boxes = [spr.collision_box for spr in sprites]
        return sprites

    def add_entity(self, entity, layer):
        entity.level = self
        self.sprites.add(entity, layer=layer)

        self.entity_added(entity)

    def remove_entity(self, entity):
        self.sprites.remove(entity)

    def entity_added(self, entity):
        for handler in self.entity_added_handlers:
            handler(entity)

    def add_entity_added_handler(self, handler):
        self.entity_added_handlers.append(handler)


