from pygame import mouse

class Handler(object):

    def __init__(self):
        self.move_handlers = []
        self.center = (400, 300)

    def handle_input(self):
        if mouse.get_pressed()[2]:
            pos = mouse.get_pos()

            rel_pos = (max(min((self.center[0] - pos[0]) / 50, 5), -5), max(min((self.center[1] - pos[1]) / 50, 5), -5))

            for h in self.move_handlers:
                h(*rel_pos)

    def add_move_handler(self, handler):
        self.move_handlers.append(handler)
