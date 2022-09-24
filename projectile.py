import pygame
from pygame.sprite import Sprite


# A class to fire projectiles from the ship and manage them
class Projectile(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.projectile_color

        # Create a projectile at the top of the ship
        self.rect = pygame.Rect(0, 0,
                                self.settings.projectile_width,
                                self.settings.projectile_height
                                )
        self.rect.midtop = game.ship.rect.midtop

        # Store bullet's position
        self.y = float(self.rect.y)

    # Move the projectile upwards
    def update(self):
        self.y -= self.settings.projectile_speed
        self.rect.y = self.y

    def draw_me(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
