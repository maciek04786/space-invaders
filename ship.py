import pygame
from pygame.sprite import Sprite


class Ship(Sprite):

    # Class to manage ships
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load("images/rocket-1374247_640.bmp")
        self.rect = self.image.get_rect()

        # Start new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for ship's horizontal position
        self.x = float(self.rect.x)

        # Movement indicator
        self.moving_right = False
        self.moving_left = False

    # Update ship's position based on movement indicator
    def update(self):
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x

    # Draw the ship
    def blit(self):
        self.screen.blit(self.image, self.rect)

    # Reposition ship back to the center of the screen
    def reset_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
