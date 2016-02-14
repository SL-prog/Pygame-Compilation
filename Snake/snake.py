import pygame
from pygame.locals import *
pygame.init()
from random import randint

fenetre = pygame.display.set_mode((0,0),FULLSCREEN)

fenetrex = fenetre.get_width()
fenetrey = fenetre.get_height()

pygame.display.set_caption("Snake")

TITLE = pygame.image.load("title.png").convert_alpha()
HEAD = pygame.image.load("head.png").convert_alpha()
BODY = pygame.image.load("body.png").convert_alpha()
FOOD = pygame.image.load("food.png").convert_alpha()

pygame.mouse.set_visible(0)

def init():
    size = 2
    snakex = [randint(160, fenetrex - 160), 0]
    snakey = [randint(160, fenetrey - 160), 0]
    snakex[1] = snakex[0]-20 #-
    snakey[1] = snakey[0]
    vx = 0
    vy = 20

    foodx = randint(160, fenetrex - 160)
    foody = randint(160, fenetrey - 160)
    return size, snakex, snakey, vx, vy, foodx, foody

hiscore = 0
SNAKE = True
menu = True
while SNAKE:
    while menu:
        score = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                menu, jeu, SNAKE = False, False, False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu, jeu, SNAKE = False, False, False
                else:
                    size, snakex, snakey, vx, vy, foodx, foody = init()
                    menu, jeu = False, True

        pygame.draw.rect(fenetre, (0,255,144), (0,0,fenetrex, fenetrey), 0) #or (205,255,255)
        fenetre.blit(TITLE, ((fenetrex/2)-260, (fenetrey/2)-201))

        font = pygame.font.Font(None, 80)
        texte = "Best : " + str(hiscore)
        txtscore = font.render(texte, 1, (255, 255, 255))
        fenetre.blit(txtscore, ((fenetrex/2)-160, (fenetrey/2)+80))

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

        if snakex[0] < 0:
            snakex[0] = fenetrex
        if snakex[0] > fenetrex:
            snakex[0] = 0
        if snakey[0] < 0:
            snakey[0] = fenetrey
        if snakey[0] > fenetrey:
            snakey[0] = 0

        if (foodx+20 >= snakex[0] >= foodx-20) and (foody+20 >= snakey[0] >= foody-20):
                foodx = randint(160, fenetrex-160)
                foody = randint(160, fenetrey-160)
                snakex = snakex + [snakex[size-1]]
                snakey = snakey + [snakey[size-1]]
                size += 1
                score += 1
                if (score > hiscore):
                    hiscore = score

        for test in range(1,size):
            if (snakex[0] == snakex[test]) and (snakey[0] == snakey[test]):
                #print("Looser") #mord  queue
                menu, jeu = True, False

        pygame.draw.rect(fenetre, (0,0,0), (0,0,fenetrex, fenetrey), 0) #fond

        fenetre.blit(HEAD, (snakex[0], snakey[0]))
        fenetre.blit(FOOD, (foodx, foody))

        for part in range(1,size):
            fenetre.blit(BODY, (snakex[part], snakey[part]))

        pygame.display.flip()
        pygame.time.Clock().tick(10)

pygame.quit()