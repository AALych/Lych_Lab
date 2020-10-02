import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 50), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100, 1)
polygon(screen, (0, 0, 0), [(180, 160), (100, 100),
                            (150, 120), (180, 140)])
polygon(screen, (0, 0, 0), [(220, 160), (300, 100),
                            (250, 120), (220, 140)])
circle(screen, (255, 100, 100), (250, 180), 20)
circle(screen, (255, 100, 100), (150, 180), 20)
circle(screen, (0, 0, 0), (250, 180), 20, 1)
circle(screen, (0, 0, 0), (150, 180), 20, 1)
circle(screen, (0, 0, 0), (250, 180), 10)
circle(screen, (0, 0, 0), (150, 180), 10)
rect(screen, (0, 0, 0), (150, 250, 100, 20))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
