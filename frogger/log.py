
from .constants import LOG_FULL
from .maths import scale_x

class Log():
    dX = scale_x(1)

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.type = 'log'

    def draw(self, win):
        win.blit(LOG_FULL, (self.x - LOG_FULL.get_width() // 2, self.y - LOG_FULL.get_height() // 2))

    def move(self):
        if self.dir == 'left':
            self.x -= self.dX
        else:
            self.x += self.dX
