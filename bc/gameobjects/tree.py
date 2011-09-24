from pygame.rect import Rect
from bc import graphics
from bc.sprite import Sprite
from bc.utils.collision_box import Collision_Box

class Tree(Sprite):
    def __init__(self, position):
        super(Tree, self).__init__(graphics.tree, position, Collision_Box(Rect(9, 0, 46, 63), self))
        self.health = 100

    def action(self):
        self.health -= 1
        if not self.health:
            print "Chopped"
