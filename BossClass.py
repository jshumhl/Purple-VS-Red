## 2D Action Role Play Game (2D ARPG)
## Created by Jonathan Shum
## Class file created to make the boss

import sys, time, random, math, pygame
from pygame.locals import *


## using list to add pics for movements to make animation 
class Boss(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None

        self.lefta = []
        self.lefta.append(pygame.transform.scale(pygame.image.load('images/boss/bal1.png').convert_alpha(), (66, 48)))
        self.lefta.append(pygame.transform.scale(pygame.image.load('images/boss/bal2.png').convert_alpha(), (66, 48)))

        self.righta = []
        self.righta.append(pygame.transform.scale(pygame.image.load('images/boss/bar1.png').convert_alpha(), (66, 48)))
        self.righta.append(pygame.transform.scale(pygame.image.load('images/boss/bar2.png').convert_alpha(), (66, 48)))

        self.num = 0
        self.image = self.master_image

    def _getx(self):
        return self.rect.x
 
    def _setx(self, value):
        self.rect.x = value

## easier movement in future
    X = property(_getx, _setx)
 
    def _gety(self):
        return self.rect.y
 
    def _sety(self, value):
        self.rect.y = value

## easier movement in future
    Y = property(_gety, _sety)
 
    def _getpos(self):
        return self.rect.topleft
 
    def _setpos(self, pos):
        self.rect.topleft = pos

## easier movement in other files
    position = property(_getpos, _setpos)

## load image
    def load(self, filename, width, height):
        self.master_image = pygame.transform.scale(pygame.image.load(filename).convert_alpha(), (48, 48))
        self.rect = Rect(0, 0, width, height)
        
    def update(self):
        self.image = self.master_image

## take pics from the list 1 by 1 and repeat to form animation
    def attackleft(self):
        self.Y -= 4
        self.image = self.lefta[self.num]
        self.num += 1
        if self.num >= len(self.lefta):
            self.num = 0
        self.Y += 4

    def attackright(self):
        self.Y -= 4
        self.image = self.righta[self.num]
        self.num += 1
        if self.num >= len(self.righta):
            self.num = 0
        self.Y += 4
