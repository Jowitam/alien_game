import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """klasa przeznaczona do zarzadzania pociskiem wystrzeliwanym przez statek"""
    def __init__(self, screen, ship, game_settings):
        """utworzenie przycisku w aktualnym polozeniu statku"""
        super().__init__()
        self.screen = screen

        # utworzenie prostokata pocisku w punkcie (0,0) oraz zdefiniowanie jego polozenia
        self.rect = pygame.Rect(0,0, game_settings.bullet_width, game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # polozenie pocisku
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update(self):
        """poruszanie pociskiem"""
        # uaktualnienie polozenia pocisku i jego prostokata
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """wyswietlanie pocisku na ekranie"""
        pygame.draw.rect(self.screen, self.color, self.rect)




