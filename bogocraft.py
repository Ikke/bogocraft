__author__ = 'ikke'

from bc.game import Game
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'

config = {
    'caption': "Bogocraft - V0.0.1"
}

g = Game(config)
g.init()
