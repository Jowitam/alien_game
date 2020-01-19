import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    """Inicjalizacja gry z utworzeniem ekranu"""
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # utworzenie statku
    ship = Ship(screen)

    # Rozpoczecie glownej petlii while w grze
    while True:
        # oczekiwanie na akcje uzytkownika
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # odswiezanie ekranu
        screen.fill(game_settings.screen_color)
        ship.blitme()

        # Wyswietlenie ekranu ostatnio zmodyfikowanego
        pygame.display.flip()

run_game()