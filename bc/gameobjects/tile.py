__author__ = 'ikke'

import pygame
from pygame import locals

class Tile(object):
    # pylint: disable-msg=E1121
    def __init__(self, coords, tile_surface):
        self.coords = coords
        self.tile_surface = tile_surface

    def render(self, surface):
        surface.blit(self.tile_surface, self.coords)
