import sys
import pygame
from pygame import  gfxdraw

pygame.init()
W = 800
H = 400
screen = pygame.display.set_mode((W, H))


def check(point):
    p = complex(0, 0)
    k = 0
    while k <= 30 and abs(p) <= 2:
        p = p*p + point
        k += 1
    if abs(p) <= 2:
        return (1, k)
    else:
        return (0, k)


def mandelbrot():
    for x in range(W):
        for y in range(H):
            z = complex(-3 + 4*x/W, -1 + 2*y/H)
            if check(z)[0]:
                gfxdraw.pixel(pygame.display.get_surface(), x, y, (255, 255, 255))
            else:
                gfxdraw.pixel(pygame.display.get_surface(), x, y, (255-check(z)[1]*8, 255-check(z)[1]*8, 255-check(z)[1]*8))


mandelbrot()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
            sys.exit(0)
    pygame.display.update()