
import pygame
from .maths import scale_x, scale_y, WIDTH, HEIGHT

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
FPS = 30

BACKGROUND = pygame.transform.scale(pygame.image.load('assets/background.gif'), (WIDTH, HEIGHT))
CAR_LEFT = pygame.transform.scale(pygame.image.load('assets/car_left.gif'), (scale_x(121), scale_y(40)))
CAR_RIGHT = pygame.transform.scale(pygame.image.load('assets/car_right.gif'), (scale_x(121), scale_y(40)))
FROG = pygame.transform.scale(pygame.image.load('assets/frog.gif'), (scale_x(40), scale_y(40)))
FROG_SMALL = pygame.transform.scale(pygame.image.load('assets/frog_small.gif'), (scale_x(20), scale_y(20)))
HOME = pygame.transform.scale(pygame.image.load('assets/home.gif'), (scale_x(50), scale_y(51)))
LOG_FULL = pygame.transform.scale(pygame.image.load('assets/log_full.gif'), (scale_x(161), scale_y(40)))
TURTLE_LEFT = pygame.transform.scale(pygame.image.load('assets/turtle_left.gif'), (scale_x(155), scale_y(40)))
TURTLE_LEFT_HALF = pygame.transform.scale(pygame.image.load('assets/turtle_left_half.gif'), (scale_x(155), scale_y(40)))
TURTLE_RIGHT = pygame.transform.scale(pygame.image.load('assets/turtle_right.gif'), (scale_x(155), scale_y(40)))
TURTLE_RIGHT_HALF = pygame.transform.scale(pygame.image.load('assets/turtle_right_half.gif'), (scale_x(155), scale_y(40)))
