
import pygame
from .constants import GREEN, FPS
from .maths import scale_x

class TimeStrip():
    dX = scale_x(2)

    def __init__(self, x, y, length, thickness):
        self.x = x
        self.y = y
        self.length = length
        self.thickness = thickness
        self.type = 'ts'
        self.counter = 0

    def draw(self, win):
        pygame.draw.rect(win, GREEN, (self.x, self.y - self.thickness // 2, self.length, self.thickness), width=0, border_radius=10)
            
    def update(self):
        self.counter += 1

        if self.counter >= FPS:
            self.counter = 0
            self.x += self.dX
            self.length -= self.dX

        if self.length <= 0:
            return True
        return False
