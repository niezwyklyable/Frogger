
from .constants import FROG, FROG_SMALL
from .maths import WIDTH, HEIGHT, scale_x, scale_y

class Frog():
    dX = WIDTH // 13
    dY = HEIGHT // 16

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        self.small_frogs = []
        self.create_sf()
        self.type = 'frog'

    def draw(self, win):
        win.blit(FROG, (self.x - FROG.get_width() // 2, self.y - FROG.get_height() // 2))
        for sf in self.small_frogs:
            win.blit(FROG_SMALL, (sf[0] - FROG_SMALL.get_width() // 2, sf[1] - FROG_SMALL.get_height() // 2))

    def move(self, dir):
        if dir == 'left':
            self.x -= self.dX
        elif dir == 'right':
            self.x += self.dX
        elif dir == 'up':
            self.y -= self.dY
        elif dir == 'down':
            self.y += self.dY

    def create_sf(self):
        x = FROG_SMALL.get_width() // 2 + scale_x(10)
        Y = scale_y(775)

        for i in range(3):
            if i != 0:
                x += FROG_SMALL.get_width() + scale_x(10)
            self.small_frogs.append((x, Y))

    def kill(self):
        self.lives -= 1
        if self.lives <= 0:
            return True
        self.small_frogs.remove(self.small_frogs[-1])
        return False
