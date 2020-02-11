import sys
import pygame
from time import sleep
from alien import Alien
from bullet import Bullet


def check_events(ship, bullets, screen, game_settings, play_button, stats, aliens, score_board):
    """reakcja na zdarzenie generowane przez mysz i klawiature"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_best_high_score(stats)
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, screen, game_settings, stats)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(play_button, mouse_x, mouse_y, stats, aliens, bullets, ship, game_settings, screen, score_board)


def check_play_button(play_button, mouse_x, mouse_y, stats, aliens, bullets, ship, game_settings, screen, score_board):
    """Rozpoczecie nowej gry po kliknieciu w przycisk GRA"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # wyzerowanie ustawien dot gry - szybkosci
        game_settings.initialize_dynamic_settings()

        # ukrycie kursora myszy
        pygame.mouse.set_visible(False)

        # wyzwerowanie danych statycznych
        stats.reset_stats()
        stats.game_active = True

        # wyzerowanie tablicy wynikow
        score_board.prep_image()

        # usuniecie obcych, pociskow
        aliens.empty()
        bullets.empty()

        # nowa flota i statek
        create_alien_fleet(game_settings, screen, aliens, ship)
        ship.center_ship()


def check_keydown_events(event, ship, bullets, screen, game_settings, stats):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, game_settings, screen, ship)
    elif event.key == pygame.K_q:
        save_best_high_score(stats)
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def fire_bullet(bullets, game_settings, screen, ship):
    """utworzenie nowego pocisku i dodanie go do grupy"""
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(screen, ship, game_settings)
        bullets.add(new_bullet)


def update_bullets(bullets, aliens, game_settings, screen, ship, stats, score_board):
    """uktualnienie polozenia pociskow i usuniecie niewidocznych na ekranie"""
    bullets.update()
    # usuniecie pocisku poza ekranem
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(aliens, bullets, game_settings, screen, ship, stats, score_board)


def check_bullet_alien_collisions(aliens, bullets, game_settings, screen, ship, stats, score_board):
    """sprawdzenie czy pocisk trafil obcego - gdy tak usuniecie obcego i pocisku"""
    colisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if colisions:
        for aliens in colisions.values():
            stats.score += game_settings.alien_points * len(aliens)
            score_board.prep_score()
        check_high_score(stats, score_board)
    start_new_level(aliens, bullets, game_settings, score_board, screen, ship, stats)


def start_new_level(aliens, bullets, game_settings, score_board, screen, ship, stats):
    """utworzenie nowej floty po zestrzeleniu oraz przyspieszenie gry oraz pozbycie sie wystrzelonych pociskow"""
    if len(aliens) == 0:
        # gdy cala flota zniszczona gracz przechodzi na kolejny poziom
        bullets.empty()
        game_settings.increase_speed()

        # inkrementacja numeru poziomu
        stats.level += 1
        score_board.prep_level()

        create_alien_fleet(game_settings, screen, aliens, ship)


def update_aliens(aliens, game_settings, ship, stats, bullets, screen, score_board):
    """sprawdzenie czy flota przy krawedzi, uaktualnienie polozenia obcych we flocie"""
    check_aliens_edges(game_settings, aliens)
    aliens.update()
    # wykrycie kolizji miedzy statkiem a obcym
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(stats, aliens, bullets, ship, game_settings, screen, score_board)
    # wyszukanie obcych ktorzy dotarli do dolnej krawedzi
    check_aliens_bottom(screen, aliens, bullets, ship, stats, game_settings, score_board)


def ship_hit(stats, aliens, bullets, ship, game_settings, screen, score_board):
    """reakcja na uderzenie obcego w statek"""
    if stats.ships_left > 0:
        # zmniejszenie liczby statkow
        stats.ships_left -= 1
        # uaktualnienie tablicy wynikow
        score_board.prep_ships()
        # usuniecie pozostalych obcych i pociskow
        aliens.empty()
        bullets.empty()
        # nowa flota i nowy statek
        create_alien_fleet(game_settings, screen, aliens, ship)
        ship.center_ship()
        # pauza
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_screen(game_settings, screen, ship, bullets, aliens, play_button, stats, score_board):
    """uaktualnienie obrazow na ekranie i przejscie do nowego ekranu"""
    # odswiezanie ekranu
    screen.fill(game_settings.screen_color)

    # ponowne wyswietlenie wszystkich pociskow pod warstwami statku kosmicznego
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    # wyswietlenie informacji o punktach
    score_board.show_score()

    # wyswietlenie przycisku tylko wtedy kiedy gra jest nieaktywna
    if not stats.game_active:
        play_button.draw_button()

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
    number_rows = int(available_space_y / (2 * alien_height))
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


def check_aliens_bottom(screen, aliens, bullets, ship, stats, game_settings, score_board):
    """sprawdzenie czy obcy dotarli do dolnej krawedzi"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats, aliens, bullets, ship, game_settings, screen, score_board)
            break


def check_high_score(stats, score_board):
    """sprawdzenie czy jest nowy najlepszy wynik"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score_board.prep_high_score()


def save_best_high_score(stats):
    """zapis najlepszego wyniku do pliku"""
    with open(stats.filname, 'w') as file_object:
        file_object.write(str(stats.high_score))
