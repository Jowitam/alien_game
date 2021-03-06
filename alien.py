import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """zarzadzanie grupa statkow obcych"""
    def __init__(self, screen, game_settings):
        """inicjalizacja obcego i jego polozenie poczatkowe"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # wczytanie obcego i jego rect - prostokata
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # obcy w lewym gornym rogu ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # dokladne polozenie obcego
        self.x = float(self.rect.x)

    def blitme(self):
        """wyswietlanie obcego w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """poruszanie floty w lewo lub prawo"""
        self.x += (self.game_settings.alien_speed_factor * self.game_settings.alien_direction)
        self.rect.x = self.x

    def check_edges(self):
        """wartosc True gdy obcy przy krawedzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True