import pygame
"""
飞船
"""
class Ship():
    def __init__(self,screen):
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False#移动标志
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    def update(self):
        """
        根据移动标志调整飞船的位置
        :return:
        """
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        elif self.moving_bottom:
            self.rect.bottom += 1
        elif self.moving_top:
            self.rect.top -= 1
    def blitem(self):
        """
             飞船初始化位置
        """
        self.screen.blit(self.image,self.rect)