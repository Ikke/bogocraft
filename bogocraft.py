__author__ = 'ikke'

import os
import pygame

config = {
    'caption': "Bogocraft - V0.0.1"
}

#os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
display = pygame.display.set_mode((800, 600))
pygame.display.set_caption(config['caption'])

from bc.game import Game

g = Game(display, config)
g.run()
