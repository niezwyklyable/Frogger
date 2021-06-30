
from .constants import TURTLE_LEFT, TURTLE_LEFT_HALF, TURTLE_RIGHT, TURTLE_RIGHT_HALF
from .maths import scale_x

class Turtle():
    dX = scale_x(1)

    def __init__(self, x, y, dir, state):
        self.x = x
        self.y = y
        self.dir = dir
        self.type = 'turtle'
        self.state = state
        self.counter = 0

    def draw(self, win):
        if self.dir == 'left':
            if self.state == 'full':
                win.blit(TURTLE_LEFT, (self.x - TURTLE_LEFT.get_width() // 2, self.y - TURTLE_LEFT.get_height() // 2))
            elif self.state == 'half' or self.state == 'half2':
                win.blit(TURTLE_LEFT_HALF, (self.x - TURTLE_LEFT_HALF.get_width() // 2, self.y - TURTLE_LEFT_HALF.get_height() // 2))
        else:
            if self.state == 'full':
                win.blit(TURTLE_RIGHT, (self.x - TURTLE_RIGHT.get_width() // 2, self.y - TURTLE_RIGHT.get_height() // 2))
            elif self.state == 'half' or self.state == 'half2':
                win.blit(TURTLE_RIGHT_HALF, (self.x - TURTLE_RIGHT_HALF.get_width() // 2, self.y - TURTLE_RIGHT_HALF.get_height() // 2))

    def move(self):
        if self.dir == 'left':
            self.x -= self.dX
        else:
            self.x += self.dX
        
        self.counter += 1
        if self.counter >= scale_x(300):
            self.counter = 0
            self.change_state()

    def change_state(self):
        if self.state == 'half2':
            self.state = 'sub'
            return
                
        states = ('sub', 'half', 'full', 'half2')
        for state in states:
            if state == self.state:
                self.state = states[states.index(state) + 1]
                break
