class Settings():
    """przechowuje wszystkie ustawienia w grze"""

    def __init__(self):
        """inicjalizacja ustawien"""
        # ustawienia ekranu
        self.screen_width = 1000
        self.screen_height = 600
        self.screen_color = (230, 230, 230)

        # ustawienia dotyczace statku
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # ustawienia pociskow bullet
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 6

        # ustawienia floty obcych
        self.alien_speed_factor = 1
        self.alien_drop_speed = 10
        # 1 poruszanie w prawo, -1 poruszanie w lewo
        self.alien_direction = 1
