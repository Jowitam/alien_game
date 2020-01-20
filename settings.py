class Settings():
    """przechowuje wszystkie ustawienia w grze"""


    def __init__(self):
        """inicjalizacja ustawien"""
        # ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.screen_color = (230, 230, 230)

        # ustawienia dotyczace statku
        self.ship_speed_factor = 1.5

        # ustawienia pociskow bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
