import pygame
import pygame.key
import logging
from bc.gameobjects.map import Map
from bc.entities.player import Player
from bc import graphics, input
#from pgu import gui

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

class Game(object):
    def __init__(self, config):
        self.config = config

        pygame.init()

        self.screen_size = (800, 600)

        self.display = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption(self.config['caption'])

        logger.debug("Displaymodes: %s" % pygame.display.list_modes(32))
        logger.debug("Displayinfo: %s" % pygame.display.Info())

        self.map = Map(30, 30)
        self.player = Player(self.screen_size, graphics.player, self.map)

    def init(self):
        clock = pygame.time.Clock()
        changed = True

        handler = input.Handler()

        handler.add_move_handler(self.player.move)

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_q:
                    return

            handler.handle_input()

            self.map.render(self.display)
            self.player.tick()

            self.player.render(self.display)

            if changed:
                pygame.display.update()
#                changed = False
            clock.tick(60)

