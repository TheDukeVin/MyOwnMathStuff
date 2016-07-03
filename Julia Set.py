
from __future__ import division
import pygame,sys
from pygame.locals import *
pygame.init()

windS = 400
Max = 100

name = 'Mandlebrot Set'

def P(a,b,ca,cb):
    return (a**2-b**2+ca,2*a*b+cb)


def color(steps):
    if steps == -1:
        return (0,0,0)
    if steps<Max/3:
        dev = int(steps*(765/Max))
        return (255-dev,dev,0)
    if steps<2*Max/3:
        dev = int(steps*(765/Max)-255)
        return (0,255-dev,dev)
    dev = int(steps*(765/Max)-510)
    return (dev,0,255-dev)

def mandle(ca,cb):
    starta = 0
    startb = 0
    steps = 0
    for i in range(0,Max):
        if starta**2+startb**2>4:
            return steps
        newa,newb = P(starta,startb,ca,cb)
        starta = newa
        startb = newb
        steps+=1
    return -1

def drawMandle(cornerx,cornery,zoom):
    pixels = pygame.PixelArray(window)
    for i in range(0,windS):
        pygame.display.update()
        for j in range(0,windS):
            pixels[i][j] = color(mandle(cornerx+i/zoom/windS,cornery+j/zoom/windS))

def julia(ca,cb,polya,polyb):
    starta = ca
    startb = cb
    steps = 0
    for i in range(0,Max):
        if starta**2+startb**2>4:
            return steps
        newa,newb = P(starta,startb,polya,polyb)
        starta = newa
        startb = newb
        steps+=1
    return -1

def drawJulia(cornerx,cornery,zoom,polya,polyb):
    pixels = pygame.PixelArray(window)
    for i in range(0,windS):
        pygame.display.update()
        for j in range(0,windS):
            pixels[i+windS][j] = color(julia(cornerx+i/zoom/windS,cornery+j/zoom/windS,polya,polyb))

def main():
    global window
    window = pygame.display.set_mode((windS*2,windS))
    pygame.display.set_caption(name)
    cornerx = -2
    cornery = -2
    zoom = 1/4
    polya = 0
    polyb = 0
    drawn = False
    drawMandle(-2,-2,1/4)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousex,mousey = event.pos
                if mousex>windS:
                    mousex-=windS
                    xshift = mousex*2/windS-1/2
                    yshift = mousey*2/windS-1/2
                    zoom*=2
                    cornerx+=xshift/zoom
                    cornery+=yshift/zoom
                    drawn = False
                else:
                    cornerx = -2
                    cornery = -2
                    zoom = 1/4
                    polya = (mousex/windS*4)-2
                    polyb = (mousey/windS*4)-2
                    drawn = False
        if drawn == False:
            drawJulia(cornerx,cornery,zoom,polya,polyb)
            drawn = True
        pygame.display.update()

if __name__ == "__main__":
    main()
