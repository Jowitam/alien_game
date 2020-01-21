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
