# coding=utf-8

class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1200    #长
        self.screen_height = 800	#宽
        self.background_color = (230,230,230)	#背景色

        #飞机设置
        # self.ship_speed_factor = 1      #飞机移动速度
        self.ship_limit = 3             #飞机可用数量

        #子弹设置
        self.bullet_width = 10
        self.bullet_height = 10
        # self.bullet_speed_factor = 3  #子弹移动速度
        self.bullet_color = 60,60,60  #子弹颜色
        self.bullets_allowed = 10         #限制未消失子弹数

        #外星人设置
        # self.alien_speed_factor = 1     #外星人移动速度
        self.fleet_drop_speed = 10      #外星人群下移速度
        #fleet_direction为1表示向右移,为-1表示向左移
        # self.fleet_direction = 1

        #动态设置加快游戏节奏
        self.speedup_scale = 1.1
        self.score_point = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.2      #飞机移动速度
        self.bullet_speed_factor = 3    #子弹移动速度
        self.alien_speed_factor = 0.5     #外星人移动速度
        #fleet_direction为1表示向右移,为-1表示向左移
        self.fleet_direction = 1

        """分值设置"""
        self.alien_point = 50


    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_point)
