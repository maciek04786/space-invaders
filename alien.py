import pygame
from pygame.sprite import Sprite


# A class representing alien ship
class Alien(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load alien image and set its rect att
        self.image = pygame.image.load("images/ufo-2121470_640.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien in the top-left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store alien's horizontal position
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
