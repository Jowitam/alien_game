import sys
import pygame


def check_events():
    """reakcja na zdarzenie generowane przez mysz i klawiature"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(game_settings, screen, ship):
    """uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # odswiezanie ekranu
    screen.fill(game_settings.screen_color)
    ship.blitme()
    # Wyswietlenie ekranu ostatnio zmodyfikowanego
    pygame.display.flip()
