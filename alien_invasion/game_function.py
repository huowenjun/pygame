import sys
import pygame
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.rect.centerx -= 1
            elif event.key == pygame.K_UP:
                ship.rect.top -= 1
            elif event.key == pygame.K_DOWN:
                ship.rect.bottom += 1
        # elif event.type == pygame.KEYUP:
        #     if event.key == pygame.K_LEFT:
        #         ship.rect.centerx -= 1
def update_screen(ai_settings,screen,ship,background):
    background.blitem() # 屏幕背景
    #screen.fill(ai_settings.bg_color)#背景色
    ship.blitem()#操作飞机
    pygame.display.flip()

