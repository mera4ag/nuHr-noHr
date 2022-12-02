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

PL1_WON = False
PL2_WON = False
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
            PL1.rect.y -= self.speed
        if keys[pygame.K_DOWN] == True:
            PL1.rect.y += self.speed
    def WS_PL2(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] == True:
            PL2.rect.y -= self.speed
        if keys[pygame.K_s] == True:
            PL2.rect.y += self.speed
#===============================================
class BALLS(GameSprite):
    global you_WON_PL1,PL1_WON, PL2_WON, you_WON_PL2
    def __init__(self, imageS, widht,height, x,y, speed):
        super().__init__(imageS, widht,height, x,y, speed)
        self.dirX = 1
        self.dirY = 1

    def BALLS_move(self):
        self.rect.x += self.speed * self.dirX
        self.rect.y += self.speed * self.dirY
        if self.rect.top <= 0:
            self.dirY = 1
        if self.rect.bottom >= win_height:
            self.dirY = -1

        if pygame.sprite.collide_rect(self, PL1):
            self.dirX = -1
        if pygame.sprite.collide_rect(self, PL2):
            self.dirX = 1

        if self.rect.x >= win_widht:
            win.blit(you_WON_PL1,(600,50))
            PL1_WON = True
            PL2_WON = False
        if self.rect. x <= 0:
            win.blit(you_WON_PL2,(100,50))
            PL1_WON = False
            PL2_WON = True

#=============================================== загрузка спрайтов
win = pygame.display.set_mode((win_widht,win_height))

bg = GameSprite(PATH + "dlyakota-4.png", win_widht,win_height, 0,0, 0)

PL1 = Player(PATH + "dlyakota-1.png", 30,150, 900,300, 15)
PL2 = Player(PATH + "dlyakota-2.png", 30,150, 100,300, 15)

ball = BALLS(PATH + "dlyakota-3.png", 50,50, 500,300, 10)
#=============================================== музыка
mus1 = pygame.mixer.Sound(PATH + '01408.wav')
mus1.play()
#=============================================== текст
color_black = (16, 16, 16)
font1 = pygame.font.SysFont('Comic Sans MS', 35)

text_pl1 = font1.render('игрок 1', True, color_black)
text_pl2 = font1.render('игрок 2', True, color_black)

you_WON_PL1 = font1.render('ПОБЕДИЛ ИГРОК 1', True, color_black)
you_WON_PL2 = font1.render('ПОБЕДИЛ ИГРОК 2', True, color_black)
#=============================================== игровой цикл
while GAME:
    events = pygame.event.get()

    bg.show()
    PL1.show()
    PL2.show()
    ball.show()

    keys = pygame.key.get_pressed()

    PL1.WS_PL1()
    PL2.WS_PL2()
    ball.BALLS_move()
    
    for event in pygame.event.get():#выход из игры при нажатия на крестик
        if event.type == pygame.QUIT:
            GAME = False

    nice_cock.tick(30)#обновление экрана
    pygame.display.update()
