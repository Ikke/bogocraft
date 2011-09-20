import pygame
import pygame.key
import logging
from bc import graphics
import bc
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

    def run(self):
        clock = pygame.time.Clock()
        changed = True

        handler = input.Handler()

        sprites = bc.utils.sprite.LayeredDirty(_time_threshold = 500)
        self.map.load_map(sprites)
        player = Player(graphics.player, (384, 278), (400,300), self.map.collision_boxes)
        handler.add_move_handler(player.move)
        sprites.add(player, layer=5)

        level = pygame.Surface((60*32+800, 60*32+600)).convert()
        sprites.draw(level)
        sprites._use_update = True


        counter = 0
        while True:
#        for i in range(5):
            counter +=1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_q:
                    return

            handler.handle_input()

            sprites.draw(level)

            self.display.blit(level, (0,0), (player.position[0], player.position[1], 800, 600))

            if changed:
                pygame.display.update()
#                changed = False
            clock.tick(40)

            if not counter % 50:
                print clock.get_fps()


