import pygame


class Ship():
    """odpowiedzialna za statek strzelajacy"""
    def __init__(self, screen):
        """inicjalizacja statku i jego polozenie na ekranie"""
        self.screen = screen

        # wczytanie statku i jego prostokata rect
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # nowy statek na dole ekranu na srodku
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """wyswietlenie statku w jego aktualnym polozeniu"""
        self.screen.blit(self.image, self.rect)
