from pygame.surface import Surface

class Entity(object):
    def __init__(self, position):
        self.current_sprite = None
        self.position = position

    def render(self, surface):
        if self.current_sprite:
            surface.blit(self.current_sprite, self.position)

