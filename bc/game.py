import pygame
import sys
# pylint: disable-msg=W0401,W0614
from pygame.locals import *
# pylint: enable-msg=W0401,W0614
import logging
from bc.gameobjects.solidtile import SolidTile
from bc.utils.coords import tile_coords as tc
from bc.gameobjects.map import Map

#from pgu import gui

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("main")

class Game(object):
    def __init__(self, config):
        self.config = config

    def init(self):
        pygame.init()

        logger.debug("Displaymodes: %s" % pygame.display.list_modes(32))
        logger.debug("Displayinfo: %s" % pygame.display.Info())

        self.surface = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(self.config['caption'])

        gamemap = Map(100, 100)

        x = 0
        y = 0

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT or event.type == KEYUP and event.key == K_q:
                    return

                if event.type == KEYUP:
                    logger.debug("Key_Up event")
                    if event.key == K_UP:
                        y += 10
                    if event.key == K_DOWN:
                        y -= 10

                    if event.key == K_RIGHT:
                        x -= 10
                    if event.key == K_LEFT:
                        x += 10

            self.surface.fill(Color('#000000'))
            gamemap.render(self.surface, (x, y, 800, 600))
            pygame.display.update()
            pygame.time.wait(5)
