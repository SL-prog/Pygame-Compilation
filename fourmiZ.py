import pygame
from pygame.locals import *
pygame.init()
from random import randint
from math import pi, cos, sin

fenetre = pygame.display.set_mode((0,0),FULLSCREEN)

crush = pygame.mixer.Sound("crush.wav")
BLOOD = pygame.image.load('blood.png').convert_alpha()

class Ant:
    def __init__(self, x, y, screenx, screeny, num):
        self.x = x
        self.y = y
        self.screenx = screenx
        self.screeny = screeny

        self.depart_timerwait, self.fin_timerwait = False, False
        self.waiting = 0
        self.depart_timermoove, self.fin_timermoove = False, False
        self.mooving = 0
        self.attendre = True
        self.bouger = False

        self.imageant = pygame.image.load("ant.png").convert_alpha()
        self.angle = randint(0,360)
        self.anglerad = self.angle*(pi/180)
        self.vx = -cos(-self.anglerad)*5
        self.vy = -sin(-self.anglerad)*5
        self.imageantangle = self.imageant
        self.q = 1
        self.changer = 0
        self.num = num
        self.killed = False


    def mouvement(self):
        if self.killed:
            return

        self.anglerad = self.angle*(pi/180)
        self.vx = -cos(-self.anglerad)*5
        self.vy = -sin(-self.anglerad)*5
        if self.q and pygame.time.get_ticks()>self.changer:
            self.angle += 5
            self.changer = pygame.time.get_ticks() + 500
            self.q = False
        if not(self.q) and pygame.time.get_ticks()>self.changer:
            self.angle -= 5
            self.q = True
            self.changer = pygame.time.get_ticks() + 500


        if self.depart_timerwait == True:
            self.waiting = pygame.time.get_ticks() + randint(250,500)
            self.depart_timerwait = False
        if self.attendre:
            if pygame.time.get_ticks() > self.waiting:
                self.fin_timerwait = True

        if self.fin_timerwait == True:
            self.bouger = True
            self.attendre = False
            self.depart_timermoove = True
            self.fin_timerwait = False

        if self.depart_timermoove == True:
            self.mooving = pygame.time.get_ticks() + randint(500,1000)
            self.depart_timermoove = False
        if self.bouger:
            if pygame.time.get_ticks() > self.mooving:
                self.fin_timermoove = True
            if pygame.time.get_ticks() <= self.mooving:
                self.x = self.x+self.vx
                self.y = self.y+self.vy

        if self.fin_timermoove == True:
            self.angle = self.angle + randint(-45,45)
            if self.angle < 0:
                self.angle = 0
            if self.angle > 360:
                self.angle = 360
            self.bouger = False
            self.attendre = True
            self.depart_timerwait = True
            self.fin_timermoove = False

        if self.x<0:
            self.x = 0
            self.angle = 180
        if self.x>self.screenx-50:
            self.x = self.screenx-50
            self.angle = 0
        if self.y<0:
            self.y = 0
            self.angle = 90
        if self.y>self.screeny-50:
            self.y = self.screeny-50
            self.angle = 270


    def affiche(self, fenetre):
        if self.killed:
            fenetre.blit(BLOOD, (self.x-15, self.y-15))
        else:
            self.rotation()
            fenetre.blit(self.imageant, (self.x, self.y)) #ant

    def rotation(self):
        self.imageant = pygame.image.load("ant.png").convert_alpha()
        origine_rectangle = self.imageant.get_rect()
        rotation_image = pygame.transform.rotate(self.imageant, self.angle)
        rotation_rectangle = origine_rectangle.copy()
        rotation_rectangle.center = rotation_image.get_rect().center
        self.imageant = rotation_image.subsurface(rotation_rectangle).copy()



pygame.display.set_caption("Fourmiz")

jeu = True
ants = []
deads = []


while jeu:
    for event in pygame.event.get():
        if event.type == QUIT:
            jeu = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                jeu = False
            if event.key == K_r:
                ants = []
        if event.type == MOUSEBUTTONDOWN and event.button == 3:
            (x, y) = pygame.mouse.get_pos()
            for a in ants:
                if x > a.x and x < a.x + 50 and y > a.y and y < a.y+50:
                    a.killed = True
                    crush.play()
                    ants.pop(a.num)
                    deads.append(a)
                    for i in ants[a.num:]:
                        i.num -= 1
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            (x, y) = pygame.mouse.get_pos()
            ants = ants + [Ant(x,y, fenetre.get_width(),fenetre.get_height(), len(ants))]

    pygame.draw.rect(fenetre, (255,255,255), (0,0,fenetre.get_width(),fenetre.get_height()), 0) #fond

    for i in deads:
        i.affiche(fenetre)

    for a in ants:
        a.mouvement()
        a.affiche(fenetre)


    pygame.display.flip()
    pygame.time.Clock().tick(30)

print(len(deads))
print(len(ants))

pygame.quit()


