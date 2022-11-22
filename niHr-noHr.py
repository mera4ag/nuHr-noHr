#=============================================== инпорт библеотек
import pygame
import os
import time
import random
pygame.init()
#=============================================== сосдание переменных
win_height = 600
win_widht = 1000

nice_cock = pygame.time.Clock()

P1_WON = False
P2_WON = False
GAME = True

PATH = ""
#=============================================== родительский класс
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, imageS, widht,height, x,y, speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imageS),(widht,height))
        self.rect = self.image.get_rect()
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    def show(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
#=============================================== 
class Player(GameSprite):
    def __init__(self, imageS, widht,height, x,y, speed):
        super().__init__(imageS, widht,height, x,y, speed)
    def WS_PL1(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] == True:
            PL1.rect.y -= 15
        if keys[pygame.K_DOWN] == True:
            PL1.rect.y += 15
    def WS_PL2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] == True:
            PL2.rect.y -= 15
        if keys[pygame.K_s] == True:
            PL2.rect.y += 15
#===============================================
class BALLS(GameSprite):
    def __init__(self, imageS, widht,height, x,y, speed):
        super().__init__(imageS, widht,height, x,y, speed)
#=============================================== загрузка спрайтов
win = pygame.display.set_mode((win_widht,win_height))

bg = GameSprite(PATH + "dlyakota-4.png", win_widht,win_height, 0,0, 0)

PL1 = Player(PATH + "dlyakota-1.png", 30,150, 900,300, 0)
PL2 = Player(PATH + "dlyakota-2.png", 30,150, 100,300, 0)

WAP = BALLS(PATH + "dlyakota-3.png", 50,50, 500,300, 5)
#=============================================== текст
color_white = (255,255,255)
#=============================================== игровой цикл
while GAME:
    events = pygame.event.get()

    bg.show()
    PL1.WS_PL1()
    PL2.WS_PL2()

    keys = pygame.key.get_pressed()

    PL1.show()
    PL2.show()
    WAP.show()

    for event in pygame.event.get():#выход из игры при нажатия на крестик
        if event.type == pygame.QUIT:
            GAME = False

    nice_cock.tick(30)#обновление экрана
    pygame.display.update()