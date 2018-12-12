import pygame
"""
背景
"""
class Background():
    def __init__(self,screen):
        self.background = pygame.image.load('images/background.jpg').convert()# 背景图
        self.screen = screen
    def blitem(self):
        self.screen.blit(self.background,(0, 0))