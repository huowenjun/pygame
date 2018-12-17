import sys
import pygame
def check_keydown_events(event,ship):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
                #ship.rect.centerx += 1
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
                # ship.rect.centerx -= 1
            elif event.key == pygame.K_UP:
                ship.moving_top = True
                # ship.rect.top -= 1
            elif event.key == pygame.K_DOWN:
                ship.moving_bottom = True
                # ship.rect.bottom += 1
def check_keyup_events(event,ship):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_top = False
                # ship.rect.top -= 1
            elif event.key == pygame.K_DOWN:
                ship.moving_bottom = False
                # ship.rect.bottom +=1

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
def update_screen(ai_settings,screen,ship,background):
    background.blitem() # 屏幕背景
    #screen.fill(ai_settings.bg_color)#背景色
    ship.blitem()#操作飞机
    pygame.display.flip()

