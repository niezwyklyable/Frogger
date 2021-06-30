
import pygame

from frogger.maths import WIDTH, HEIGHT
from frogger.game import Game
from frogger.constants import FPS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frogger v1.0 by AW')

def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)

    # sterowanie ciagłe nieliniowe (domyslnie, bez wpisywania tej komendy, sterowanie punktowe)
    pygame.key.set_repeat(500, 50) # generuje impulsy KEYDOWN po odpowiednim czasie w ms 
    # podczas trzymania danego przycisku (*args) -> (pierwszy, kazdy nastepny)
    # lub tez (opoznienie, interwal)
    # z wlasnego doswiadczenia interval powinien stanowic 10% delay'a

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

            if event.type == pygame.KEYDOWN:
                if not game.gameover:
                    if event.key == pygame.K_LEFT:
                        game.frog.move('left')
                    elif event.key == pygame.K_RIGHT:
                        game.frog.move('right')
                    elif event.key == pygame.K_UP:
                        game.frog.move('up')
                    elif event.key == pygame.K_DOWN:
                        game.frog.move('down')

        # sterowanie ciagłe liniowe bezopoznieniowe (natychmiastowe), bezinterwałowe (najszybsze)
        #keys = pygame.key.get_pressed() # zwraca slownik z wartosciami typu bool

        #if not game.gameover:
        #    if keys[pygame.K_LEFT]:
        #        game.frog.move('left')
        #    elif keys[pygame.K_RIGHT]:
        #        game.frog.move('right')
        #    elif keys[pygame.K_UP]:
        #        game.frog.move('up')
        #    elif keys[pygame.K_DOWN]:
        #        game.frog.move('down')

        game.update()
        game.render()

    pygame.quit()

main()
