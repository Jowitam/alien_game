import sys
import pygame


def check_events(ship):
    """reakcja na zdarzenie generowane przez mysz i klawiature"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def update_screen(game_settings, screen, ship):
    """uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # odswiezanie ekranu
    screen.fill(game_settings.screen_color)
    ship.blitme()
    # Wyswietlenie ekranu ostatnio zmodyfikowanego
    pygame.display.flip()
