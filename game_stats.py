class GameStats():
    """monitorowanie danych statycznych gry"""
    # plik z najlepszym wynikiem
    filname = 'best_high_score.txt'

    def __init__(self, game_settings):
        """inicjalizacja danych statycznych"""
        self.game_settings = game_settings
        self.reset_stats()
        # stan aktywny gry
        self.game_active = False
        # najlepszy wynik
        self.high_score = self.high_score_ever(self.filname)

    def reset_stats(self):
        """inicjalizacja danych statycznych ktore zmieniaja sie w trakcie gry"""
        self.ships_left = self.game_settings.ship_limit
        self.score = 0
        self.level = 1

    def high_score_ever(self, filname):
        with open(filname) as file_object:
            high_score = file_object.read()
        return int(high_score)
