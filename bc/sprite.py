import pygame
import bc.utils.sprite

class Sprite(bc.utils.sprite.DirtySprite):
    def __init__(self, image, position):
        super(Sprite, self).__init__()
        self.image = image
        self.rect = pygame.Rect(0,0,0,0)

        _, _, width, height = self.image.get_rect()
        self.rect = pygame.Rect(position[0], position[1], width, height)




