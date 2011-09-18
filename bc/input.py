from pygame import mouse

class Handler(object):

    def __init__(self):
        self.move_handlers = []
        self.center = (400, 300)

    def handle_input(self):
        if mouse.get_pressed()[2]:
            pos = mouse.get_pos()

            rel_pos = ((self.center[0] - pos[0]) / 50, (self.center[1] - pos[1]) / 50)

            print rel_pos
            for h in self.move_handlers:
                h(*rel_pos)

    def add_move_handler(self, handler):
        self.move_handlers.append(handler)
