class Settings:
    """przechowuje wszystkie ustawienia w grze"""

    def __init__(self):
        """inicjalizacja ustawien"""
        # ustawienia ekranu
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_color = (230, 230, 230)

        # ustawienia dotyczace statku
        self.ship_limit = 3

        # ustawienia pociskow bullet
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # ustawienia floty obcych
        self.alien_drop_speed = 10

        # zmiana szybkosci gry
        self.speedup_scale = 1.1

        # zmiana liczby punktow
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """inicjalizacja ustawien zmieniajacych sie w trakcie gry"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # 1 poruszanie w prawo, -1 poruszanie w lewo
        self.alien_direction = 1

        # punktacja
        self.alien_points = 20

    def increase_speed(self):
        """zmiana szybkosci gry oraz ilosci punktow"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
