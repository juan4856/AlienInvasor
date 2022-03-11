class Settings():

    def __init__(self):
        #Inicializa las configuracionesd el juego

        self.screen_width = 1200
        self.screen_high= 800
        self.bg_color = (230,230,230)

        #Bullet Settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_high = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #Ship Settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        

        #Aliens settigns
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #Fleet_director of 1 represents righ; -1 represents left
        self.fleet_direction = 1
