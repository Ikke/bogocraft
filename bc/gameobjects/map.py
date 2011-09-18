import logging
import pygame.surface
from bc import graphics
from bc.utils.alternator import Alternator

logger = logging.getLogger('map')

class Map(object):
    def __init__(self, width, height):
        self.tiles = []
        self.map = None

        alternator = Alternator(graphics.grass, graphics.dirt)

        for x in range(0, width):
            self.tiles.append([])
            for y in range(0, height):
                tile = ((x * 32, y * 32), alternator.get())
                self.tiles[x].append(tile)

        self.view = (0, 0, width * 32, height * 32)

    def move_view(self, x, y):
        self.view = (self.view[0] + x, self.view[1] + y, self.view[2], self.view[3])
        print self.view

    def render(self, screen):
        """
        Renders the map to the screen
        @param screen Surface
        """
        if self.map is None:
            self.map = pygame.surface.Surface((1000,1000))
            self.map.convert()

            for rows in self.tiles:
                for tile in rows:
                    self.map.blit(tile[1], tile[0])

        screen.blit(self.map, (0, 0), self.view)
