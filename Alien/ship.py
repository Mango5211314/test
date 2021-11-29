import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self, al_settings, screen):
        '''初始化飞船并设置其初始位置'''
        super(Ship, self).__init__()
        self.screen = screen
        self.al_settings = al_settings
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load(r'image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 将每艘飞船放置在屏幕中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        # 在飞船的属性center中储存小数值
        self.center = float(self.rect.centerx)
    def updata(self):
        '''根据移动标志调整飞船的位置'''
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.al_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.al_settings.ship_speed_factor
        #根据self.center的值更新rect对象
        self.rect.centerx = self.center
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''让飞船在屏幕上居中'''
        self.center = self.screen_rect.centery