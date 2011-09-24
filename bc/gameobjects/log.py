from bc import graphics
from bc.sprite import Sprite

class Log(Sprite):
    def __init__(self, position):
        super(Log, self).__init__(graphics.log, position)

    def action(self):
        print "Not implemented yet"
