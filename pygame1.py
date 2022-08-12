#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import pygame as py
from sys import exit 

py.init()

screen = py.display.set_mode((800,400))
py.display.set_caption("My First Game Ever")
clock = py.time.Clock()
font1 = py.font.Font("pyg/Pixeltype.ttf", 50)



# positional setup


mouse_pos = py.mouse.get_pos()

# speed setup
snail_step = 4
char_step = 4
step = 5

# other setup
snail_face = 1
char_face = 1
score = 0
char_speed = 20
line_end_pos = (0,0)
gravity = 0


#sky
sky_pos_x = 0
sky_pos_y = 300

sky_surf = py.image.load("pyg/Sky.png").convert_alpha()
sky_rect = sky_surf.get_rect(midbottom = (sky_pos_x,sky_pos_y))

#ground
ground_pos_x = 0
ground_pos_y = 300

ground_surf = py.image.load("pyg/ground.png").convert_alpha()
ground_rect = ground_surf.get_rect(midtop = (ground_pos_x,ground_pos_y))


#enemy1
snail_pos_x = 0
snail_pos_y = ground_pos_y
snail_surf = py.image.load("pyg/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (snail_pos_x, snail_pos_y))


#char
char_pos_x = 450
char_pos_y = ground_pos_y
char_surf = py.image.load("pyg/char.png").convert_alpha()
char_rect = char_surf.get_rect(midbottom = (char_pos_x, char_pos_y))


#test pointer
pointer_pos_x= 0
pointer_pos_y= ground_pos_y-1
pointer_surf = py.Surface((10,10))
pointer_surf.fill("red")
pointer_rect = pointer_surf.get_rect(midbottom = (pointer_pos_x, pointer_pos_y))







# chars patrol & bounce from walls
def bounce(pos_rect_x, step, face):
    
    if pos_rect_x <= 0:
        face = 1
    elif pos_rect_x >= 800:
        face = -1    
    pos_rect_x += (face*step)
    return pos_rect_x, face


# mouse chasing def
def mouse_chase (x_pos, y_pos, mousepos, step):    
    if x_pos < mousepos[0]:
        x_pos += step
    elif x_pos > mousepos[0]:
        x_pos -= step

    if y_pos < mousepos[1]:
        y_pos += step
    elif y_pos > mousepos[1]:
        y_pos -= step
    return x_pos, y_pos
        
# will be added to class: action  - function name: jump    
def jump():
    pass

# main loop
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            exit()
#Class - Game Mechanics: mouse button down: I did not use it in anywhere YET
        if event.type == py.MOUSEBUTTONDOWN:
            line_end_pos = event.pos

#Class - Game Mechanics: jump on press space            
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                gravity = -20
                
#Class - Game Mechanics: go left on press D button
        if event.type == py.KEYDOWN:
            if event.key == py.K_d:
                char_rect.right += char_speed

#Class - Game Mechanics: go right on press A button
        if event.type == py.KEYDOWN:
            if event.key == py.K_a:
                char_rect.left -= char_speed

        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                 char_speed += 1 
        if event.type == py.KEYDOWN:
            if event.key == py.K_s:
                char_speed -= 1

    
# background blit    
    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf,(ground_pos_x,ground_pos_y))

# text
    text1_render = font1.render ("Position Of DOT " + str(mouse_pos[0]) + "," + str(mouse_pos[1]), True, "Black")
    text1_rect = text1_render.get_rect(topleft = (5, 5))
    screen.blit(text1_render,text1_rect)
    
    text2_render = font1.render ("Position Of Char: " + str(char_rect[0]) + " , " +str(char_rect[1]), True, "Black")
    text2_rect = text2_render.get_rect(topleft = (5, 60))
    screen.blit(text2_render,text2_rect)

    text3_render = font1.render ("Score: " + str(score), True, "Black")
    py.draw.rect(screen, "red", (text3_rect[0],text3_rect[1], score, text3_rect[3]))
    text3_rect = text3_render.get_rect(topleft = (5, 115))
    screen.blit(text3_render,text3_rect)

    text4_render = font1.render ("Char Speed: " + str(char_speed), True, "Black")
    text4_rect = text4_render.get_rect(topleft = (5, 165))
    screen.blit(text4_render,text4_rect)

    
    
# ENEMY

# enemy blit
    screen.blit(snail_surf,snail_rect)
    
#enemy patrol & bounce from walls
    snail_rect.left, snail_face = bounce(snail_rect.left,snail_step, snail_face)

    
    
#CHAR

# char blit
   
    
# char falls down after jump
#    while char_rect.y < ground_pos_y:
    gravity += 1
    char_rect.y += gravity
    
    if char_rect.bottom > ground_rect.top:
        char_rect.bottom = ground_rect.top
    screen.blit(char_surf,char_rect)
# pointer blit
    mouse_pos = py.mouse.get_pos()
    screen.blit(pointer_surf,(pointer_pos_x,pointer_pos_y))
# def to move the pointer
    pointer_pos_x, pointer_pos_y = mouse_chase(pointer_pos_x,pointer_pos_y,mouse_pos, step)
    
    
# score    
    if char_rect.colliderect(snail_rect):
        score += 1
        
    if char_rect.collidepoint(pointer_pos_x, pointer_pos_y):
        score -= 1

# closing of the loop        
    py.display.update()
    clock.tick(60)


# In[ ]:





# In[ ]:




