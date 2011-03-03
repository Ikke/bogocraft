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

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT or event.type == KEYUP and event.key == K_q:
                    return

            self.surface.fill(Color('#000000'))

            pygame.display.update()
            pygame.time.wait(25)
