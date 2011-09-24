import math
from pygame import mouse

class Handler(object):

    def __init__(self):
        self.move_handlers = []
        self.center = (400, 300)
        self.action_handlers = []
        self.mouse_down = False

    def handle_input(self):
        if mouse.get_pressed()[2]:
            pos = mouse.get_pos()
            max_speed = 4


            rel_pos = (max(min((self.center[0] - pos[0]) / 50, max_speed), -max_speed),
                       max(min((self.center[1] - pos[1]) / 50, max_speed), -max_speed))

            for h in self.move_handlers:
                h(*rel_pos)

        if mouse.get_pressed()[0]:
            self.mouse_down = True
            pos = mouse.get_pos()

            distance = int(math.sqrt(abs(pos[0] - self.center[0]) ** 2 + abs(pos[1] - self.center[1]) ** 2))

            if distance < 100:
                for h in self.action_handlers:
                    h(pos)
        else:
            self.mouse_down = False

    def add_move_handler(self, handler):
        self.move_handlers.append(handler)

    def add_action_handler(self, handler):
        self.action_handlers.append(handler)

