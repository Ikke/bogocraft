__author__ = 'ikke'

import pygame
from pygame import locals

class SolidTile(object):
    # pylint: disable-msg=E1121
    def __init__(self, coords, color=(255,255,255)):
        self.coords = coords
        self.tile = pygame.Surface((33,33))
        self.tile.set_colorkey((0,0,0))
        pygame.draw.polygon(self.tile, color, [(16, 0), (32, 16), (16, 32), (0, 16)], 0)

    def render(self, surface):
        surface.blit(self.tile, self.coords)
