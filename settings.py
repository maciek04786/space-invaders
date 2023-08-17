class Settings:
    # Class to store all settings for the game

    def __init__(self):
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship
        self.ship_speed = 1.0
        self.ship_limit = 3

        # Alien
        self.fleet_drop_speed = 10
        self.alien_speed = 0.25
        # Direction of 1 represents right, - 1 represents left
        self.fleet_direction = 1

        # Projectile
        self.projectile_speed = 1.0
        self.projectile_width = 3
        self.projectile_height = 12
        self.projectile_color = (200, 255, 0)
        self.projectiles_allowed = 10

        # Levels
        self.level_up_scale = 1.1
        self.alien_points = 50
        self.score_increase = 1.5

    def increase_level(self):
        self.ship_speed *= self.level_up_scale
        self.alien_speed *= self.level_up_scale
        self.projectile_speed *= self.level_up_scale
        self.alien_speed *= self.level_up_scale
        self.alien_points = round(self.alien_points * self.score_increase)
