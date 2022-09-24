class StatsManager:

    # Tracks statistics and info for the game
    def __init__(self, game):
        self.settings = game.settings
        self.ships_remaining = self.settings.ship_limit
        self.score = 0
        with open("high-score", mode="r") as file:
            self.high_score = int(file.read())
        self.game_on = True
