import pygame
import sys
from pygame.locals import *
import logging
from bc.gameobjects.tile import Tile
from bc.utils.coords import tile_coords as tc

#from pgu import gui

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")

class Game(object):
    def __init__(self, config):
        self.config = config

    def init(self):
        pygame.display.init()

        logger.debug("Displaymodes: %s" % pygame.display.list_modes(32))
        logger.debug("Displayinfo: %s" % pygame.display.Info())

        self.surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(self.config['caption'])

        tiles_absolute = [
                Tile((0,0)), Tile((16,16)), Tile((32, 32)),
                Tile((-16, 16)), Tile((0, 32))
        ]

        tiles_relative = [
                Tile(tc(0,0)), Tile(tc(1,0)), Tile(tc(2,0)), Tile(tc(-1,-1)),
                Tile(tc(0,1)), Tile(tc(0, 2)), Tile(tc(1,1))
        ]

        tiles = []
        for x in range(0, 19):
          tiles.append(Tile(tc(x - 1, x)))

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT or event.type == KEYUP and event.key == K_q:
                    return

            self.surface.fill(Color('#000000'))
            for tile in tiles:
                tile.render(self.surface)

            pygame.display.update()
            pygame.time.wait(25)
