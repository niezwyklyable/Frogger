
from .constants import HOME, FROG

class Home():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.empty = True
        self.type = 'home'

    def draw(self, win):
        if self.empty:
            win.blit(HOME, (self.x - HOME.get_width() // 2, self.y - HOME.get_height() // 2))
        else:
            win.blit(HOME, (self.x - HOME.get_width() // 2, self.y - HOME.get_height() // 2))
            win.blit(FROG, (self.x - FROG.get_width() // 2, self.y - FROG.get_height() // 2))
