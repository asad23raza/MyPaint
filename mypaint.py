# Working with Pygame
import pygame
from pygame.locals import *
pygame.init()
font = pygame.font.SysFont('Georgia',24)
font2 = pygame.font.SysFont('Georgia',18)
class Colours:
    white= 255,255,255
    red= 255,0,0
    teal  = 0,128,128
    yellow= 255,255,0
    orange= 255,215,0
    purple= 128,0,128
    green= 0,255,0
    blue= 0,0,255
    lime = 0,255,0
    black = 0,0,0
# Title
title = font.render("MyPaint! ",1, Colours.black)
controls = font2.render("Key: R:Red, B:Blue, G:Green, O:Orange,P:Purple, L:Lime ",1, Colours.black)
controls2 = font2.render("Press E to Erase and Space to stop drawing",1, Colours.black)
# Global Variables
width = 800
height = 800
window = pygame.display.set_mode((width,height))
window.fill(Colours.white)
window.blit(title, (width / 2 - title.get_width() / 2, 5))
window.blit(controls, (width / 2 - controls.get_width() / 2, title.get_height() + 5))
window.blit(controls2, (width / 2 - controls2.get_width() / 2, title.get_height() + controls.get_height() + 5))
pygame.display.update()
###
# Function to Draw a Circle
def draw(window, tup=(400,400), colour=(0,0,0)):
    pygame.draw.circle(window, colour, 
                        tup, 4)
    pygame.display.update()
def reset_screen(window):
    pygame.draw.rect(window, Colours.white, (0,100,800,800))
    pygame.display.update()

run = True
ink = False
colour = 0,0,0
keydict = {
    K_g: Colours.green,
    K_b: Colours.blue,
    K_w: Colours.white,
    K_t: Colours.teal,
    K_y: Colours.yellow,
    K_o: Colours.orange, 
    K_p: Colours.purple, 
    K_l: Colours.lime,
    K_r: Colours.red,
    K_k: Colours.black
}
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == MOUSEMOTION:
                if ink:
                    pos = pygame.mouse.get_pos()
                    if pos[1] >= 100:
                        draw(window, pygame.mouse.get_pos(), colour)
        elif event.type == KEYDOWN:
            if event.key in keydict:
                print('reached2')
                ink = True
                colour = keydict[event.key]
            elif event.key == K_SPACE:
                ink = False
            elif event.key == K_e:
                ink = True
                colour = Colours.white
            elif event.key == K_x:
                reset_screen(window)


