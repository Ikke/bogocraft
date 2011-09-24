import logging
import pygame.surface
import pygame
from bc import graphics, sprite
from bc.gameobjects.tree import Tree

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


        for k in range(100):
            spr = sprite.Sprite(graphics.forrest, (600 + k % 10 * self.tile_size[0], 600 + k // 10 * self.tile_size[1]))
            sprite_group.add(spr, layer=0)

        trees = [
            Tree((630, 687)),
            Tree((750, 710)),
            Tree((830, 790)),
            Tree((630, 845)),
            Tree((915, 841)),
            Tree((601, 638)),
            Tree((787, 957)),
            Tree((840, 681)),
            Tree((678, 900)),
            Tree((716, 834))

        ]
        sprite_group.add(trees, layer=2)

        self.collision_boxes = [spr.collision_box for spr in trees]
        return sprite_group
