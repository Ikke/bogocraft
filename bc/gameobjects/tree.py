from pygame.rect import Rect
from bc import graphics, sounds
from bc.gameobjects.log import Log
from bc.sprite import Sprite
from bc.utils.collision_box import Collision_Box

class Tree(Sprite):
    def __init__(self, position):
        super(Tree, self).__init__(graphics.tree, position, True, Collision_Box(Rect(22, 45, 18, 18), self))
        self.health = 100

    def action(self):
        self.health -= 1

        if not self.health % 20:
            sounds.chop.play()

        if not self.health:
            self.level.remove_entity(self)

            log = Log((self.rect.centerx, self.rect.centery))
            self.level.add_entity(log)
