class GameStats():
    """monitorowanie danych statycznych gry"""

    def __init__(self, game_settings):
        """inicjalizacja danych statycznych"""
        self.game_settings = game_settings
        self.reset_stats()
        # stan aktywny gry
        self.game_active = False
        # najlepszy wynik
        self.high_score = 0

    def reset_stats(self):
        """inicjalizacja danych statycznych ktore zmieniaja sie w trakcie gry"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
