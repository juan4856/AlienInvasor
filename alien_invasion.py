import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
import game_functions as gf



def run_game():
    # inicializa el juego y crea un objeto pantalla
    pygame.init()
    ai_settings= Settings()
    screen = pygame.display.set_mode((
    ai_settings.screen_width,ai_settings.screen_high))
    pygame.display.set_caption("Alien Invasor")

    # Create an instance to store game statistics.
    stats = GameStats(ai_settings)
    #Make ship and an alien
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings, screen)
    #Make group of bullets and aliens
    bullets = Group()
    aliens = Group()

    #Create the fleat of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    

    while True:


        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen, ship, aliens, bullets)

run_game()

