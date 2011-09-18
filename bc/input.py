from pygame import mouse

class Handler(object):

    def __init__(self):
        self.move_handlers = []
        self.mouse = False

    def handle_input(self):
        print mouse.get_pressed()[2]
        if mouse.get_pressed()[2]:
            if not self.mouse:
                for h in self.move_handlers:
                    h(-5,0)
            self.mouse = True
        else:
            self.mouse = False

    def add_move_handler(self, handler):
        self.move_handlers.append(handler)
