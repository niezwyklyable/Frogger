
import pygame
from .constants import BACKGROUND, CAR_LEFT, LOG_FULL, TURTLE_LEFT, FROG, HOME, BLACK
from .maths import scale_x, scale_y, WIDTH, HEIGHT
from .home import Home
from .frog import Frog
from .car import Car
from .log import Log
from .turtle import Turtle
from .timestrip import TimeStrip
pygame.init() # potrzebne do pygame.font

class Game():
    def __init__(self, win):
        self.win = win
        self.homes = []
        self.frog = None
        self.cars = []
        self.logs = []
        self.turtles = []
        self.time_strip = None
        self.create_homes()
        self.create_frog()
        self.create_cars()
        self.create_logs()
        self.create_turtles()
        self.create_time_strip()
        self.gameover = False

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))

        for home in self.homes:
            home.draw(self.win)

        for car in self.cars:
            car.draw(self.win)

        for log in self.logs:
            log.draw(self.win)

        for turtle in self.turtles:
            turtle.draw(self.win)

        if self.frog:
            self.frog.draw(self.win)

        self.time_strip.draw(self.win)

        if self.gameover:
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render('You win!', 1, BLACK)
            self.win.blit(text, (int(WIDTH / 2 - text.get_width() / 2), int(HEIGHT / 2 - text.get_height() / 2)))

        pygame.display.update()

    def create_homes(self):
        self.homes = []
        x = scale_x(100)
        Y = scale_y(125)
        for _ in range(5):
            self.homes.append(Home(x, Y))
            x += scale_x(100)

    def create_frog(self):
        self.frog = Frog(WIDTH // 2, scale_y(725))

    def create_cars(self):
        y = scale_y(675)

        for i in range(5):
            if i % 2 == 0:
                dir = 'left'
                x = WIDTH + scale_x(-100)
            else:
                dir = 'right'
                x = scale_x(100)

            self.cars.append(Car(x, y, dir))
            self.cars.append(Car(x + scale_x(300), y, dir))
            y -= scale_y(50)

    def create_logs(self):
        y = scale_y(375)

        for i in range(5):
            if i == 2 or i == 3:
                y -= scale_y(50)
                continue

            if i % 2 == 0:
                dir = 'left'
                x = WIDTH + scale_x(-100)
            else:
                dir = 'right'
                x = scale_x(100)

            self.logs.append(Log(x, y, dir))
            self.logs.append(Log(x + scale_x(300), y, dir))
            y -= scale_y(50)

    def create_turtles(self):
        y = scale_y(275)

        for i in range(2):
            if i % 2 == 0:
                dir = 'left'
                x = WIDTH + scale_x(-100)
                state = 'half'
            else:
                dir = 'right'
                x = scale_x(100)
                state = 'full'

            self.turtles.append(Turtle(x, y, dir, state))
            self.turtles.append(Turtle(x + scale_x(300), y, dir, state))
            y -= scale_y(50)

    def create_time_strip(self):
        X = scale_x(320)
        Y = scale_y(775)
        LENGTH = scale_x(120)
        THICKNESS = scale_y(5)
        self.time_strip = TimeStrip(X, Y, LENGTH, THICKNESS)

    def update(self):
        for car in self.cars:
            car.move()
            self.check_edges(car)
        for log in self.logs:
            log.move()
            self.check_edges(log)
        for turtle in self.turtles:
            turtle.move()
            self.check_edges(turtle)

        if self.frog:
            self.check_edges(self.frog)
            self.check_collisions_with_frog()
        
        if not self.gameover:
            if self.time_strip.update():
                self.frog.x = WIDTH // 2
                self.frog.y = scale_y(725)
                self.create_time_strip()
                if self.frog.kill():
                    self.create_homes()
                    self.create_frog()

            for home in self.homes:
                if home.empty:
                    break
            else:
                self.gameover = True
                self.frog = None

    def check_edges(self, obj):
        if obj.type == 'car':
            car = obj
            if car.dir == 'left':
                if car.x <= -CAR_LEFT.get_width() // 2:
                    car.x = WIDTH + CAR_LEFT.get_width() // 2
            elif car.dir == 'right':
                if car.x >= WIDTH + CAR_LEFT.get_width() // 2:
                    car.x = -CAR_LEFT.get_width() // 2
        elif obj.type == 'log':
            log = obj
            if log.dir == 'left':
                if log.x <= -LOG_FULL.get_width() // 2:
                    log.x = WIDTH + LOG_FULL.get_width() // 2
            elif log.dir == 'right':
                if log.x >= WIDTH + LOG_FULL.get_width() // 2:
                    log.x = -LOG_FULL.get_width() // 2
        elif obj.type == 'turtle':
            turtle = obj
            # TURTLE_LEFT ma taki sam rozmiar jak obrazki w pozostalych stanach
            if turtle.dir == 'left':
                if turtle.x <= -TURTLE_LEFT.get_width() // 2:
                    turtle.x = WIDTH + TURTLE_LEFT.get_width() // 2
            elif turtle.dir == 'right':
                if turtle.x >= WIDTH + TURTLE_LEFT.get_width() // 2:
                    turtle.x = -TURTLE_LEFT.get_width() // 2
        elif obj.type == 'frog':
            frog = obj
            if frog.x <= -FROG.get_width() // 2 or frog.x >= WIDTH + FROG.get_width() // 2 or \
                frog.y > scale_y(725):
                frog.x = WIDTH // 2
                frog.y = scale_y(725)
                self.create_time_strip()
                if frog.kill():
                    self.create_homes()
                    self.create_frog()

    def check_collisions_with_frog(self):
        frog = self.frog

        for car in self.cars:
            if car.x - CAR_LEFT.get_width() // 2 < frog.x + FROG.get_width() // 2 and car.x + CAR_LEFT.get_width() // 2 > frog.x - FROG.get_width() // 2 and car.y == frog.y:
                frog.x = WIDTH // 2
                frog.y = scale_y(725)
                self.create_time_strip()
                if frog.kill():
                    self.create_homes()
                    self.create_frog()

        for log in self.logs:
            if log.x - LOG_FULL.get_width() // 2 < frog.x + FROG.get_width() // 2 and log.x + LOG_FULL.get_width() // 2 > frog.x - FROG.get_width() // 2 and log.y == frog.y:
                if log.dir == 'left':
                    frog.x -= log.dX
                else:
                    frog.x += log.dX
                break
        else:
            for turtle in self.turtles:
                if turtle.state != 'sub' and \
                    turtle.x - TURTLE_LEFT.get_width() // 2 < frog.x + FROG.get_width() // 2 and turtle.x + TURTLE_LEFT.get_width() // 2 > frog.x - FROG.get_width() // 2 and turtle.y == frog.y:
                    if turtle.dir == 'left':
                        frog.x -= turtle.dX
                    else:
                        frog.x += turtle.dX
                    break
            else:
                for home in self.homes:
                    if home.x - HOME.get_width() // 2 < frog.x + FROG.get_width() // 2 and home.x + HOME.get_width() // 2 > frog.x - FROG.get_width() // 2 and home.y == frog.y:
                        home.empty = False
                        frog.x = WIDTH // 2
                        frog.y = scale_y(725)
                        self.create_time_strip()
                        break
                else:
                    if frog.y <= scale_y(375):
                        frog.x = WIDTH // 2
                        frog.y = scale_y(725)
                        self.create_time_strip()
                        if frog.kill():
                            self.create_homes()
                            self.create_frog()
