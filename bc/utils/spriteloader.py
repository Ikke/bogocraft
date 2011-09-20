import pygame
from pygame.surface import Surface

class SpriteLoader(object):
    def __init__(self, path, grid_size = (32, 32)):
        self.sprites = pygame.image.load(path).convert_alpha()
        self.grid_size = grid_size

    def get(self, x, y, sprite_size = (1, 1)):
        sprite_width = sprite_size[0] * self.grid_size[0]
        sprite_height = sprite_size[1] * self.grid_size[1]

        sprite_surface = self.sprites.subsurface(((x * self.grid_size[0], y * self.grid_size[1],
                     sprite_width, sprite_height)))

        #sprite = Sprite(sprite_surface)

        return sprite_surface
