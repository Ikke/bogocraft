import pygame
import pygame.key
import logging
from bc import graphics
from bc.gameobjects.map import Map
from bc.entities.player import Player
from bc import input
#from pgu import gui

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("main")

class Game(object):
    def __init__(self, display, config):
        self.config = config
        self.display = display

        pygame.init()

        self.screen_size = (800, 600)

        self.map = Map()
        self.player = Player(graphics.player, (384, 278), (400,300))

        self.map.move_view(100, 100)

    def run(self):
        clock = pygame.time.Clock()
        changed = True

        handler = input.Handler()

        handler.add_move_handler(self.player.move)

        sprites = pygame.sprite.LayeredDirty()
        self.map.load_map(sprites)
        sprites.add(self.player, layer=5)

        level = pygame.Surface((60*32+800, 60*32+600)).convert()

        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_q:
                    return

            handler.handle_input()

            sprites.draw(level)

            self.display.blit(level, (0,0), (self.player.position[0], self.player.position[1], 800, 600))

            if changed:
                pygame.display.update()
#                changed = False
            clock.tick(60)
            print "FPS: %s" % clock.get_fps()

