import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


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
        gf.check_events()

        gf.update_screen(game_settings, screen, ship)




run_game()