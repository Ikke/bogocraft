__author__ = 'ikke'
import pygame

class SolidTileSurface(object):
    def __init__(self, color):
        self.tile = pygame.Surface((33,33))
        self.tile.set_colorkey((0,0,0))
        pygame.draw.polygon(self.tile, color, [(16, 0), (32, 16), (16, 32), (0, 16)], 0)

    def render(self, surface, coords):
        surface.blit(self.tile, coords)
