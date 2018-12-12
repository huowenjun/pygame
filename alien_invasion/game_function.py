import sys
import pygame
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship,background):
    background.blitem() # 屏幕背景
    #screen.fill(ai_settings.bg_color)#背景色
    ship.blitem()#操作飞机
    pygame.display.flip()