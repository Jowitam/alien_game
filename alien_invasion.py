import pygame
from pygame.sprite import Group

from alien import Alien
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
    ship = Ship(screen, game_settings)

    # utworzenie grupy pociskow
    bullets = Group()

    # utworzenie obcego
    alien = Alien(screen, game_settings)

    # Rozpoczecie glownej petlii while w grze
    while True:
        gf.check_events(ship, bullets, screen, game_settings)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(game_settings, screen, ship, bullets, alien)




run_game()
