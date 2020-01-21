import sys
import pygame

from alien import Alien
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


def check_keydown_events(event, ship, bullets, screen, game_settings):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, game_settings, screen, ship)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(bullets, game_settings, screen, ship):
    # utworzenie nowego pocisku i dodanie go do grupy
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(screen, ship, game_settings)
        bullets.add(new_bullet)


def update_bullets(bullets):
    """uktualnienie polozenia pociskow i usuniecie niewidocznych na ekranie"""
    bullets.update()
    # usuniecie pocisku poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_aliens(aliens, game_settings):
    """sprawdzenie czy flota przy krawedzi, uaktualnienie polozenia obcych we flocie"""
    check_aliens_edges(game_settings, aliens)
    aliens.update()


def update_screen(game_settings, screen, ship, bullets, aliens):
    """uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # odswiezanie ekranu
    screen.fill(game_settings.screen_color)

    # ponowne wyswietlenie wszystkich pociskow pod warstwami statku kosmicznego
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # Wyswietlenie ekranu ostatnio zmodyfikowanego
    pygame.display.flip()


def create_alien_fleet(game_settings, screen, aliens, ship):
    """stworzenie pelnej floty obcych"""
    # stworzenie obcego i ustalenie odleglosci miedzy nimi
    alien = Alien(screen, game_settings)
    number_aliens_x = get_number_aliens_x(alien.rect.width, game_settings)
    number_rows = get_number_rows(game_settings, alien.rect.height, ship.rect.height)

    # stworzenie floty obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # tworzenie obcego w rzedzie i postawienie na ekranie
            create_alien(alien_number, aliens, game_settings, screen, row_number)


def create_alien(alien_number, aliens, game_settings, screen, row_number):
    """utworzenie obcego i umieszczenie go w rzedzie"""
    alien = Alien(screen, game_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_aliens_x(alien_width, game_settings):
    """ustalenie liczby obcych w rzedzie"""
    available_space_x = game_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(game_settings, alien_height, ship_height):
    """ustalenie liczy rzedow na ekranie od statku dwa rzedy wolne"""
    available_space_y = (game_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows


def check_aliens_edges(game_settings, aliens):
    """reakcja na dotarcie obcego do krawedzi"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_alien_direction(game_settings, aliens)
            break

def change_alien_direction(game_settings, aliens):
    """przesuniecie obcych w dol i zmiana kierunku"""
    for alien in aliens.sprites():
        alien.rect.y += game_settings.alien_drop_speed
    game_settings.alien_direction *= -1
