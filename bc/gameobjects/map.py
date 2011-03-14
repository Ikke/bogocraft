from solidtile import SolidTile
from bc.utils.coords import tile_coords
import logging
import pygame.surface

logger = logging.getLogger('map')

class Alternater(object):
    def __init__(self, *kargs):
        self.options = kargs
        self.current = 0

    def get(self):
        index = self.current
        self.current = (self.current + 1) % len(self.options)
        return self.options[self.current]
    
    def set(self, new_index):
        self.current = new_index % len(self.options)
        
class Map(object):
    colors = [(30,30,30), (255,255,255)]
    def __init__(self, width, height):
        self.tiles = []
        columns = Alternater(0, 1)
        rows = Alternater(*self.colors)

        self.map = None

        for x in range(0, width):
            self.tiles.append([])
            rows.set(columns.get())
            for y in range(0, height):
                self.tiles[x].append(SolidTile(tile_coords(x+12, y-12), rows.get()))

    def render(self, screen, view):
        if self.map is None:
            self.map = pygame.surface.Surface((1000,1000))
            self.map.convert()

            for rows in self.tiles:
                for tile in rows:
                    tile.render(self.map)

        screen.blit(self.map, (0, 0), view)
