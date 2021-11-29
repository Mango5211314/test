class GameStats():
    '''跟踪游戏的统计信息'''
    def __init__(self, al_settings):
        '''初始化统计信息'''
        self.al_settings = al_settings
        self.reset_stats()
        # 游戏刚启动时处于非活动状态
        self.game_active = False
        # 在任何情况下都不会重置的最高得分
        self.high_score = 0

    def reset_stats(self):
        '''初始化在游戏运行期间可能变化的统计信息'''
        self.ship_left = self.al_settings.ship_limit
        self.score = 0
        self.level = 1
