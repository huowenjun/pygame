import sys
import pygame
from settings import Settings
def run_game():
    pygame.init()
    ai_settings = Settings()
    scree = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )#幕布
    pygame.display.set_caption(ai_settings.name)#游戏名称
    # bg_color = (230,230,230)#背景色

    #开始游戏的主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        scree.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()