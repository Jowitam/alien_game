import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
    """Inicjalizacja gry z utworzeniem ekranu"""
    pygame.init()
    game_settings = Settings()

    screen = pygame.display.set_mode((game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    # utworzenie przycisku GRA
    play_button = Button(game_settings, screen, "Gra")

    # utworzenie objektu do przechowywania danych statycznych
    stats = GameStats(game_settings)

    # utworzenie statku, grupy pociskow oraz grupy obcych
    ship = Ship(screen, game_settings)
    bullets = Group()
    aliens = Group()

    # utworzenie floty obcych
    gf.create_alien_fleet(game_settings, screen, aliens, ship)

    # Rozpoczecie glownej petlii while w grze
    while True:
        gf.check_events(ship, bullets, screen, game_settings, play_button, stats)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, game_settings, screen, ship)
            gf.update_aliens(aliens, game_settings, ship, stats, bullets, screen)

        gf.update_screen(game_settings, screen, ship, bullets, aliens, play_button, stats)


run_game()
