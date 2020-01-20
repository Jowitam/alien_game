import sys
import pygame
from bullet import Bullet

def check_events(ship, bullets, screen, game_settings):
    """reakcja na zdarzenie generowane przez mysz i klawiature"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, screen, game_settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_keydown_events(event, ship, bullets, screen, game_settings):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # utworzenie nowego pocisku i dodanie go do grupy
        if len(bullets) < game_settings.bullets_allowed:
            new_bullet = Bullet(screen, ship, game_settings)
            bullets.add(new_bullet)


def update_screen(game_settings, screen, ship, bullets):
    """uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # odswiezanie ekranu
    screen.fill(game_settings.screen_color)

    # ponowne wyswietlenie wszystkich pociskow pod warstwami statku kosmicznego
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    # Wyswietlenie ekranu ostatnio zmodyfikowanego
    pygame.display.flip()
