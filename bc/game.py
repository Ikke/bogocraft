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
        self.player_position_on_screen = (384, 278)
        self.player_position_in_game = (16, 20)

        self.input_handler = input.Handler()
        self.sprites = bc.utils.sprite.LayeredDirtyPosition(_time_threshold = 500)

        self.player = Player(graphics.player, self.player_position_on_screen, self.player_position_in_game)
        self.map = self.load_map(self.sprites, self.player)

        self.initialize_player(self.player)


    def load_map(self, sprites, player):
        map = Map(sprites)
        map.add_entity_added_handler(player.sprite_added)
        map.add_entity_removed_handler(player.sprite_removed)
        map.load_map()

        self.level = pygame.Surface((60*32+800, 60*32+600)).convert()

        sprites.draw(self.level)
        sprites._use_update = True

        return map

    def initialize_player(self, player):
        self.input_handler.add_move_handler(player.move)
        self.input_handler.add_action_handler(player.action)
        self.sprites.add_movable_object(player, layer=5)


    def draw_interface(self):
        border_color = (90, 40, 1)
        interface_color = (100, 100, 100)
        background_color = (22, 22, 22)

        self.display.fill(background_color)

        pygame.draw.line(self.display, border_color, (800, 0), (800, 600))
        pygame.draw.line(self.display, border_color, (0, 600), (800, 600))

        pygame.draw.rect(self.display, interface_color, (150, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (192, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (234, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (276, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (318, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (360, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (402, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (444, 605, 40, 40), 1)
        pygame.draw.rect(self.display, interface_color, (486, 605, 40, 40), 1)



    def run(self):
        clock = pygame.time.Clock()

        player = self.player

        counter = 0
        while True:
            counter +=1

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYUP and event.key == pygame.K_q:
                    return

            self.input_handler.handle_input()
            self.sprites.draw(self.level)

            self.draw_interface()

            self.display.blit(self.level, (0,0), (player.position[0], player.position[1], 800, 600))

            pygame.display.update()

            clock.tick(60)

            if not counter % 50:
                print clock.get_fps()


