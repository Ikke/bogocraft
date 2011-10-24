from bc import graphics
from bc.sprite import Sprite

class Log(Sprite):
    def __init__(self, position):
        super(Log, self).__init__(graphics.log, position, True)
        self.action_performed = False

    def action(self):
        if not self.action_performed:
            print "Not implemented yet"
            self.action_performed = True
