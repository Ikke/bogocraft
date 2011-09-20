import logging
import pygame.surface
import pygame
from bc import graphics, sprite

logger = logging.getLogger('map')

class Map(object):
    def __init__(self, size = (60, 60), tile_size = (32, 32)):

        self.size = size
        self.tile_size = tile_size

        self.view = (0, 0, self.size[0] * self.tile_size[0], self.size[1] * self.tile_size[1])

    def move_view(self, x, y):
        self.view = (max(min(self.view[0] + x, 1920), 0), max(min(self.view[1] + y, 1920), 0), self.view[2], self.view[3])
        #print self.view


    def load_map(self, sprite_group):
        for k in range(0, self.size[0] * self.size[1]):
            spr = sprite.Sprite(graphics.grass, (400 + k % self.size[0] * self.tile_size[0],
                                                 300 + k // self.size[1] * self.tile_size[1]))
            sprite_group.add(spr, layer=0)

        tree = sprite.Sprite(graphics.tree, (400, 500))
        sprite_group.add(tree, layer=2)

        return sprite_group
