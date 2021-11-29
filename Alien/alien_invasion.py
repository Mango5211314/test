import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    al_settings = Settings()
    screen = pygame.display.set_mode((al_settings.screen_width, al_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(al_settings, screen, 'Play')
    # 创建一个用于存储游戏统计信息的实例并创建记分牌
    stats = GameStats(al_settings)
    sb = Scoreboard(al_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(al_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人
    aliens = Group()
    # 创建外星人群
    gf.creat_fleet(al_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(al_settings, screen, stats, play_button, ship, aliens, bullets,sb)
        if stats.game_active:
            ship.updata()
            gf.updata_bullets(al_settings, screen, ship, aliens, bullets, stats, sb)
            gf.update_aliens(al_settings, stats, screen, ship, aliens, bullets,sb)
        gf.updata_screen(al_settings, screen, ship, bullets, aliens, play_button, stats, sb)

run_game()