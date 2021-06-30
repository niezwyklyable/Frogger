
from .constants import CAR_LEFT, CAR_RIGHT
from .maths import scale_x

class Car():
    dX = scale_x(2)

    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.type = 'car'

    def draw(self, win):
        if self.dir == 'left':
            win.blit(CAR_LEFT, (self.x - CAR_LEFT.get_width() // 2, self.y - CAR_LEFT.get_height() // 2))
        else:
            win.blit(CAR_RIGHT, (self.x - CAR_RIGHT.get_width() // 2, self.y - CAR_RIGHT.get_height() // 2))

    def move(self):
        if self.dir == 'left':
            self.x -= self.dX
        else:
            self.x += self.dX
