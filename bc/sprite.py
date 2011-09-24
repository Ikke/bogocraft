import pygame
from bc.utils.collision_box import Collision_Box
import bc.utils.sprite

class Sprite(bc.utils.sprite.DirtySprite):
    def __init__(self, image, position, collision_box = None):
        super(Sprite, self).__init__()
        self.image = image
        self.rect = pygame.Rect(0,0,0,0)

        _, _, width, height = self.image.get_rect()
        self.rect = pygame.Rect(position[0], position[1], width, height)

        if collision_box:
            collision_box.rect.move_ip(*position)
            self.collision_box = collision_box
        else:
            self.collision_box = Collision_Box(self.rect, self)




