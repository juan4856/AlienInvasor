class GameStats():
    """Track Statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Inicialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start alien invasion in an active state.
        self.game_active = True

    def reset_stats(self):
        """Inicialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit