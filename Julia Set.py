
from __future__ import division
import pygame,sys
from pygame.locals import *
pygame.init()

windS = 400
editS = 200
Max = 100

name = 'Julia Set'

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

def julia(ca,cb,polya,ployb):
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

def draw(cornerx,cornery,zoom,polya,polyb):
    pixels = pygame.PixelArray(window)
    for i in range(0,windS):
        pygame.display.update()
        for j in range(0,windS):
            pixels[i][j] = color(julia(cornerx+i/zoom/windS,cornery+j/zoom/windS,polya,polyb))

def write(phrase,color,size_word,center):
    font = pygame.font.Font('freesansbold.ttf',size_word)
    surf = font.render(phrase,True,color)
    rect = surf.get_rect()
    rect.center = center
    window.blit(surf,rect)

def edit():
    
def main():
    global window
    window = pygame.display.set_mode((windS,windS+editS))
    pygame.display.set_caption(name)
    cornerx = -2
    cornery = -2
    zoom = 1/4
    drawn = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mousex,mousey = event.pos
                if 0<mousex<windS/2:
                    xshift = 0
                else:
                    xshift = 1
                if 0<mousey<windS/2:
                    yshift = 0
                else:
                    yshift = 1
                xshift = mousex*2/windS-1/2
                yshift = mousey*2/windS-1/2
                zoom*=2
                cornerx+=xshift/zoom
                cornery+=yshift/zoom
                drawn = False
        if drawn == False:
            draw(cornerx,cornery,zoom)
            drawn = True
        pygame.display.update()

if __name__ == "__main__":
    main()

