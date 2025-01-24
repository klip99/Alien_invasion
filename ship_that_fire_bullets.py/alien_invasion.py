

import pygame
from pygame.sprite import Group 
from settings import Settings
from ship import Ship
import game_funtions as gf
from alien import Alien
from game_stats import GameStats
from button import Button
from score_board import Scoreboard


def run_game():
    
    # Initialize game and create a screen.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
   # Initialize game clocking speed.
    clock = pygame.time.Clock()

    # Instances of game classes.
    ship = Ship(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    stats = GameStats(ai_settings) 
    play_button = Button(ai_settings, screen, "PLAY")
    score_b = Scoreboard(ai_settings, screen, stats)

    # Group instances of bullets and aliens.
    bullets = Group()
    aliens = Group()
    
    # A fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Main loop for the game.
    while True:
        
        # Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, stats, score_b, play_button, ship, bullets, aliens)
       
        if stats.game_active:
            ship.update()
           
            #gf.write_score(stats, score_b)
        
        # Get rid of bullets that have disappeared.
            gf.update_bullets(ai_settings, screen, stats, score_b, ship, aliens, bullets)

        # Update alien movement.
            gf.update_aliens(ai_settings, stats, score_b, screen, ship, aliens, bullets)
        
        # Redraw the screen during each pass through the loop.
        gf.update_screen(ai_settings, stats, score_b, screen, ship, aliens, bullets, play_button)
        

    # Game speed.
    clock.tick(120)

run_game()

