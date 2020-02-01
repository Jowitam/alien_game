import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """odpowiedzialna za statek strzelajacy"""

    def __init__(self, screen, game_settings):
        """inicjalizacja statku i jego polozenie na ekranie"""
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings

        # wczytanie statku i jego prostokata rect
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # nowy statek na dole ekranu na srodku
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # punkt srodkowy statku
        self.center = float(self.rect.centerx)

        # poruszanie statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """uaktualnienia polozenia statku na podstawie opcji wskazujacej na jego ruch"""
        # uaktualnienie wartosci punktu srodkowego statku a nie jego prostokata
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.game_settings.ship_speed_factor

        # uaktualnienie obiektu rect na podstawie center
        self.rect.centerx = self.center

    def blitme(self):
        """wyswietlenie statku w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """umieszczenie statku na srodku na dole ekranu"""
        self.center = self.screen_rect.centerx