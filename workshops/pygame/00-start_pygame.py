import pygame as pg
from random import randint as rand

pg.init()

#Define some colors
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

colors = [black, white, green, red]

width = 700
height = 500
FPS = 240
screen = pg.display.set_mode((width,height))
pg.display.set_caption("ComProg ECN")
clock = pg.time.Clock()



xi, yi = (0,0)
xf, yf = (0,0)
col=0
### TODO 2 (change static boolean -> variable) ###
while True:
##############
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            ### TODO 3 (stop running) ###

            ##############
            pg.quit()
    
    ### TODO 4 (check condition)###

    screen.fill(colors[col]);col+=1;col%=len(colors)
    

    # Draw text "ComProg ECN" [size : 80 , center :(width/2 , height/4)]
    font_name = pg.font.match_font('arial') # กำหนดชื่อ Font
    font = pg.font.Font(font_name, 80) # กำหนดขนาด font
    text_surface = font.render("ComProg ECN", True, black) # กำหนด Text และ สี
    text_rect = text_surface.get_rect() # แปลง Surface เป็น object
    text_rect.midtop = (400, 300) # ระบุตำแหน่งของ text
    screen.blit(text_surface, text_rect) # เอา Text ใส่ลงใน object ของ Text นั้น

    pg.draw.rect(screen, red,[xi,yi,xf,yf],0)
    pg.draw.line(screen, green ,[xi,yi],[xf,yf],5)
    pg.draw.ellipse(screen , black , [xi,yi,xf,yf], 2)
    xi+=rand(1,9);xi%=700
    xf+=rand(1,9);xi%=700
    # yi+=rand(1,9);yi%=700
    # yf+=rand(1,9);yf%=700
    
    pg.display.flip()

