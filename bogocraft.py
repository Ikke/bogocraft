__author__ = 'ikke'

import pygame
import cProfile
import argparse
import sys

parser = argparse.ArgumentParser(description="Start bogocraft")

parser.add_argument("--profile", dest="profile", default=False, help="Enables profile output", nargs="?")
parser.add_argument('-p', dest='profile', default='profile.out')
args = parser.parse_args()

config = {
    'caption': "Bogocraft - V0.0.1"
}

#os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
display = pygame.display.set_mode((1000, 650))
pygame.display.set_caption(config['caption'])

from bc.game import Game

g = Game(display, config)

if not args.profile:
    cProfile.run('g.run()', args.profile or "profile.out")
else:
    g.run()
