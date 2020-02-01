import pygame.font


class Scoreboard:
    """przedstawienie informacji o punktacji"""

    def __init__(self, screen, game_settings, stats):
        """inicjalizacja atrybutow dotyczacych punktacji"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.game_settings = game_settings
        self.stats = stats

        # ustawienia czcionki dla punktacji
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # poczatkowy obraz z punktacja
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """przeksztalcenie punktacji na wygenerowany obraz"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.game_settings.screen_color)

        # punktacja w prawym gornym. rogu
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """wyswietlanie punktacji na ekranie"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """najlepszy wynik w grze na obrazie"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.game_settings.screen_color)

        # najlepszy wynik w na gorze na srodku ekranu
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top
