import pygame
from pygame.draw import *
import math
import random as r
#import numpy as np

pygame.init()

FPS = 30


def house(x, y, k, n, m):
    polygon(screen, (255, 165, 0), ((x, y), (x + k, y), (x + k, y - 2 * n),
                                    (x - k, y - 2 * n), (x - k, y), (x, y)))
    polygon(screen, (0, 0, 0), ((x, y), (x + k, y), (x + k, y - 2 * n),
                                (x - k, y - 2 * n), (x - k, y), (x, y)), 1)
    polygon(screen, (200, 0, 0), ((x, y - 2 * n), (x + (k + 10), y - 2 * n), (x, y - 3 * n),
                                  (x - (k + 10), y - 2 * n), (x, y - 2 * n)))
    polygon(screen, (0, 0, 0), ((x, y - 2 * n), (x + (k + 10), y - 2 * n), (x, y - 3 * n),
                                (x - (k + 10), y - 2 * n), (x, y - 2 * n)), 1)
    circle(screen, (173, 216, 230), (x, y - n), m)
    circle(screen, (255, 255, 255), (x, y - n), m, 1)
    line(screen, (255, 255, 255), (x, y - n + m), (x, y - n - m), 1)
    line(screen, (255, 255, 255), (x + m, y - n), (x - m, y - n), 1)


#def sun(x, y, r, g, b):
    #for i in range(37):
        #c = i * np.pi / 36
        #polygon(screen, (r, g, b), ((int(x + 50 * np.cos(c)), int(y - 50 * np.sin(c))),
                                    #(int(x + 50 * np.cos(np.pi * 2 / 3 + c)),
                                     #int(y - 50 * np.sin(np.pi * 2 / 3 + c))),
                                    #(int(x + 50 * np.cos(np.pi * 4 / 3 + c)),
                                     #int(y - 50 * np.sin(np.pi * 4 / 3 + c)))))


def cloud(x, y, r):
    for i in range(1, 5):
        circle(screen, (255, 255, 255), (x + r * i, y), r)
        circle(screen, (0, 0, 0), (x + i * r, y), r, 1)
    for i in range(1, 3):
        circle(screen, (255, 255, 255), (x + r * (i + 1), y - r), r)
        circle(screen, (0, 0, 0), (x + (i + 1) * r, y - r), r, 1)


def tree(x, y, l, wid, r):
    polygon(screen, (139, 69, 19), ((x, y), (x + wid, y), (x + wid, y + 2 * l),
                                    (x - wid, y + 2 * l), (x - wid, y), (x, y)))
    for k in range(1, 3):
        circle(screen, (0, 255, 0), (x, y - 3 * r), r)
        circle(screen, (0, 0, 0), (x, y - 3 * r), r, 1)
        circle(screen, (0, 255, 0), (x - r, y - 2 * r), r)
        circle(screen, (0, 0, 0), (x - r, y - 2 * r), r, 1)
        circle(screen, (0, 255, 0), (int(x + 0.6 * r), y - 2 * r), r)
        circle(screen, (0, 0, 0), (int(x + 0.6 * r), y - 2 * r), r, 1)
        y += int(1.5 * r)


screen = pygame.display.set_mode((800, 600))
rect(screen, (135, 206, 250), (0, 0, 800, 350))
rect(screen, (0, 255, 127), (0, 350, 800, 250))
house(150, 430, 110, 75, 45)
tree(550, 270, 60, 15, 40)
tree(700, 290, 65, 14, 39)
tree(480, 300, 55, 13, 37)
house(380, 520, 100, 60, 35)
cloud(200, 100, 35)
cloud(580, 90, 40)
cloud(50, 50, 25)



#sun(100, 100, 255, 255, 0)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
