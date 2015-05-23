import pygame
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Jeu des 10min")

jeu = True
x1 = 245
y1 = 245
x3 = 245
y3 = 245
pygame.key.set_repeat(1, 1)
pygame.mouse.set_visible(0)
while jeu:
    (x2, y2) = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            jeu = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT and x1>0:
                x1 = x1 - 5
            if event.key == K_RIGHT and x1<480:
                x1 = x1 + 5
            if event.key == K_UP and y1>0:
                y1 = y1 - 5
            if event.key == K_DOWN and y1<480:
                y1 = y1 + 5
            if event.key == K_a and x3>0:
                x3 = x3 - 5
            if event.key == K_d and x3<480:
                x3 = x3 + 5
            if event.key == K_w and y3>0:
                y3 = y3 - 5
            if event.key == K_s and y3<480:
                y3 = y3 + 5

    pygame.draw.rect(fenetre, (255,255,255), (0,0,500,500), 0) #fond

    pygame.draw.rect(fenetre, (0,156,200), (x1,y1,20,20), 0) #perso
    pygame.draw.rect(fenetre, (255,156,200), (x2,y2,30,30), 0) #perso
    pygame.draw.rect(fenetre, (0,156,200), (x3,y3,20,20), 0) #perso
    perso1 = pygame.Rect(x1, y1,20, 20)
    perso2 = pygame.Rect(x2, y2,30, 30)
    perso3 = pygame.Rect(x3, y3,20, 20)

    if perso1.colliderect(perso2) or perso3.colliderect(perso2):
        jeu=False
    pygame.display.flip()

pygame.quit()