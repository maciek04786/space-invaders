import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:

    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont("consolas", 20)
        self.prep_ships()
        self.prep_score()
        self.prep_high_score()
        self.ships = Group()
        self.score_image = None
        self.score_rect = None
        self.high_score_image = None
        self.high_score_rect = None


    def prep_ships(self):
        for ship_number in range(self.stats.ships_remaining):
            ship = Ship(self.game)
            ship.image = pygame.image.load("images/rocket-1374247_640_small.bmp")
            ship.rect = ship.image.get_rect()
            ship.rect.left = 5 + ship_number * ship.rect.width
            ship.rect.top = 5
            self.ships.add(ship)

    def prep_score(self):
        score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top = 10

    def prep_high_score(self):
        high_score_str = "{:,}" .format(self.stats.high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right - 10
        self.high_score_rect.top = 10


    def display_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            with open("high-score", mode="w") as file:
                file.write(str(self.stats.high_score))
            self.prep_high_score()
