class Settings():
    '''存储外星人的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # 飞船设置
        self.ship_speed_factor = 0.1
        self.ship_limit = 3
        # 子弹设置
        self.bullet_speed_factor = 2
        self.bullet_width = 100
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 50
        # 外星人设置
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 1
        # 以什么样的节奏加快游戏进度
        self.speedup_scale = 0.5
        # 外星人点数提高的速度
        self.score_scale = 1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的量的设置'''
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 积分
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
