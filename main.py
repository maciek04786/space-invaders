import sys
import pygame
import time
from ship import Ship
from settings import Settings
from projectile import Projectile
from alien import Alien
from game_stats import StatsManager
from scoreboard import Scoreboard


# Class managing the game assets and behaviour
class SpaceInveyders:

    # Initialize the game and create resources
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Space Inveyders")
        self.stats = StatsManager(self)
        self.scoreboard = Scoreboard(self)
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.projectiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_alien_fleet()

    # Check mouse or keyboard events
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Check if any keys have been pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self.fire_projectile()

            # Check if any keys have been depressed
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    # Update images on the screen and flip to the new screen
    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blit()
        for projectile in self.projectiles.sprites():
            projectile.draw_me()
        self.aliens.draw(self.screen)
        self.scoreboard.display_score()
        pygame.display.flip()

    def update_projectiles(self):
        self.projectiles.update()

        # Remove projectiles from outside screen
        for projectile in self.projectiles.copy():
            if projectile.rect.bottom < 0:
                self.projectiles.remove(projectile)

        # Remove projectiles and aliens which have collided
        if pygame.sprite.groupcollide(self.projectiles, self.aliens, True, True):
            self.stats.score += self.settings.alien_points
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        # Check if there's any aliens remaining, if not, create a new fleet
        if not self.aliens:
            self.projectiles.empty()
            self.create_alien_fleet()
            self.settings.increase_level()

    def fire_projectile(self):
        if len(self.projectiles) < self.settings.projectiles_allowed:
            new_projectile = Projectile(game)
            self.projectiles.add(new_projectile)

    # Create single alien, determine its position and add it to alien sprite group
    def create_alien(self, alien_n, row_n):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width) * alien_n
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien.rect.height) * row_n
        self.aliens.add(alien)

    # Create a new fleet of aliens
    def create_alien_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Determine the number of aliens in a row and the number of rows
        available_x_space = self.settings.screen_width - (3 * alien_width)
        number_x_aliens = round(available_x_space / (2 * alien_width))
        ship_height = self.ship.rect.height
        available_y_space = self.settings.screen_height - (3 * alien_height) - (2 * ship_height)
        number_rows = round(available_y_space / (2 * alien_height))

        for row_n in range(number_rows):
            for alien_n in range(number_x_aliens):
                self.create_alien(alien_n, row_n)

    # Check if any alien ship reached the edge of the screen
    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    # Check if any aliens reached the bottom of the screen
    def check_fleet_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit()
                break

    # Change direction after reaching screen border
    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
        self.check_fleet_bottom()

    # Respond to alien-ship collision, by removing all aliens and bullets and resetting ship's position
    def ship_hit(self):
        if self.stats.ships_remaining > 0:
            self.stats.ships_remaining -= 1
            self.scoreboard.prep_ships()
            self.aliens.empty()
            self.projectiles.empty()
            self.create_alien_fleet()
            self.ship.reset_ship()
            time.sleep(1)
        else:
            self.stats.game_on = False


    def run_game(self):
        while True:
            self.check_events()

            if self.stats.game_on:
                self.ship.update()
                self.update_aliens()
                self.update_projectiles()
            self.update_screen()



if __name__ == "__main__":
    game = SpaceInveyders()
    game.run_game()
