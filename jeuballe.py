import pygame
from pygame.locals import *
pygame.init()

class Balle:
    def __init__(self, x, y, vx, vy, color, screenx, screeny):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.screenx = screenx
        self.screeny = screeny
        red = ((self.x/self.screenx)*255)
        if red > 255:
            red = 255
        if red < 0:
            red = 0
        blue = ((self.y/self.screeny)*255)
        if blue > 255:
            blue = 255
        if blue < 0:
            blue = 0
        self.couleur = (red, color, blue)
        self.q = 1

    def mouvement(self):
        self.x = self.x+self.vx
        self.y = self.y+self.vy
        if self.x<0:
            self.vx = 5
        if self.x>self.screenx-20:
            self.vx = -5
        if self.y<0:
            self.vy = 5
        if self.y>self.screeny-20:
            self.vy = -5

    def affiche(self, fenetre):
        pygame.draw.ellipse(fenetre, self.couleur, (self.x, self.y,20,20), 0) #balle
        pygame.draw.ellipse(fenetre, (0,0,0), (self.x, self.y,20,20), 1) #balle

    def esquive(self):
        (xmouse, ymouse) = pygame.mouse.get_pos()
        if xmouse >= self.x and xmouse <= self.x+20 and ymouse >= self.y and ymouse <= self.y+20:
            if self.q:
                self.vx = -self.vx
                self.q=0
            else:
                self.vy = -self.vy
                self.q=1


color = int(input("Style couleur ? (0-255) :"))

fenetre = pygame.display.set_mode((0,0),FULLSCREEN)

pygame.display.set_caption("Balle")

jeu = True
numero = 0
balle = []


if color < 0:
    color = 0
if color > 255:
    color = 255

while jeu:
    for event in pygame.event.get():
        if event.type == QUIT:
            jeu = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                jeu = False
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            (x, y) = pygame.mouse.get_pos()
            balle = balle + [Balle(x+5,y-5,5,-5,color,fenetre.get_width(),fenetre.get_height())]
            numero = numero + 1
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            balle = []
            numero = 0

    pygame.draw.rect(fenetre, (255,255,255), (0,0,fenetre.get_width(),fenetre.get_height()), 0) #fond

    for rang in range(numero):
        balle[rang].mouvement()
        balle[rang].esquive()
        balle[rang].affiche(fenetre)



    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()


