import pygame
from pygame.locals import *
pygame.init()
from random import randint

fenetre = pygame.display.set_mode((0,0),FULLSCREEN)

pygame.display.set_caption("Snake")

head = pygame.image.load("head.png").convert_alpha()
body = pygame.image.load("body.png").convert_alpha()

def init():
    size = 2
    snakex = [randint(160, fenetre.get_width() - 160), 0]
    snakey = [randint(160, fenetre.get_height() - 160), 0]
    snakey[1] = snakex[0]-20
    snakey[1] = snakey[0]
    vx = 0
    vy = 20
    return size, snakex, snakey, vx, vy

SNAKE = True
menu = True
while SNAKE:
    while menu:
        for event in pygame.event.get():
            if event.type == QUIT:
                menu, jeu, SNAKE = False, False, False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu, jeu, SNAKE = False, False, False
                else:
                    size, snakex, snakey, vx, vy = init()
                    menu, jeu = False, True

        pygame.draw.rect(fenetre, (205,255,255), (0,0,fenetre.get_width(),fenetre.get_height()), 0) #fond

        pygame.display.flip()


    while jeu:
        for event in pygame.event.get():
            if event.type == QUIT:
                jeu, SNAKE = False, False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    jeu, SNAKE = False, False
                if event.key == K_UP:
                    vx = 0
                    vy= -20
                if event.key == K_DOWN:
                    vx = 0
                    vy= 20
                if event.key == K_LEFT:
                    vx = -20
                    vy = 0
                if event.key == K_RIGHT:
                    vx = 20
                    vy= 0
                if event.key == K_RETURN:
                    snakex = snakex + [snakex[size-1]]
                    snakey = snakey + [snakey[size-1]]
                    size += 1

        for part in range(size-1,0,-1):
            snakex[part] = snakex[part-1]
            snakey[part] = snakey[part-1]

        snakex[0] = snakex[0]+vx
        snakey[0] = snakey[0]+vy

        for test in range(1,size):
            if (snakex[0] == snakex[test]) and (snakey[0] == snakey[test]):
                print("Looser")
                menu, jeu = True, False

        pygame.draw.rect(fenetre, (255,255,255), (0,0,fenetre.get_width(),fenetre.get_height()), 0) #fond

        fenetre.blit(head, (snakex[0], snakey[0]))

        for part in range(1,size):
            fenetre.blit(body, (snakex[part], snakey[part]))

        pygame.display.flip()
        pygame.time.Clock().tick(10)

pygame.quit()