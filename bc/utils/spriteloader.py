import pygame
from pygame.surface import Surface

class SpriteLoader(object):
    def __init__(self, path, grid_size = (32, 32)):
        self.sprites = pygame.image.load(path)
        self.grid_size = grid_size

    def get(self, x, y, sprite_size = (1, 1)):
        sprite_width = sprite_size[0] * self.grid_size[0]
        sprite_height = sprite_size[1] * self.grid_size[1]

        sprite = pygame.surface.Surface((sprite_width,sprite_height))
        sprite.set_colorkey((255, 0, 255))

        sprite.blit(self.sprites, (0,0),
                    (x * self.grid_size[0], y * self.grid_size[1],
                     sprite_width, sprite_height))
        return sprite
