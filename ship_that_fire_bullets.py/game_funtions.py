import pygame, sys
from bullets import Bullet
from alien import Alien
from ship import Ship
from time import sleep

def check_keydown_events(event, ai_settings, stats, screen, score_b, ship, bullets):
   
    """Responds to keypresses events"""
    keys = pygame.key.get_pressed()
    
    if keys [pygame.K_RIGHT]:
        ship.moving_right = True
        
    elif keys [pygame.K_LEFT]:
        ship.moving_left = True
        
    elif keys [pygame.K_UP]:
        ship.moving_up = True
        
    elif keys [pygame.K_DOWN]:
        ship.moving_down = True

    elif keys [pygame.K_q]:
        
        sys.exit()    
       
    elif keys [pygame.K_a]:
        fire_bullet(ai_settings, screen, ship, bullets)
        
    elif keys [pygame.K_p]:
        stats.game_active = True
       
    elif keys [pygame.K_o]:
        stats.game_active = False
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) <= ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    
    # Responds to key release.
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
        
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
        
    elif event.key == pygame.K_UP:
        ship.moving_up = False
        
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False 
         
def check_events(ai_settings, screen, stats, score_b, play_button, ship, bullets, aliens):
    
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
            # KEY_DOWN EVENTS.
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, stats, screen, score_b, ship, bullets)

            # KEY RELEASE RESPONSES.
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
        elif event.type == pygame.MOUSEBUTTONDOWN :
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, stats, score_b, play_button, bullets, aliens, mouse_x, mouse_y)
                   
def check_play_button(ai_settings, screen, ship, stats, score_b, play_button, bullets, aliens, mouse_x, mouse_y):
    
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        stats.game_active = True

         
        # Reset the scoreboard images.
        score_b.prep_score()
        score_b.prep_high_score()
        score_b.prep_level()
        score_b.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)
      
def update_screen(ai_settings, stats, score_b, screen, ship, aliens, bullets, play_button):
   
    # Backround images for the game.
    scaled_bg = pygame.transform.scale(ai_settings.bg_image,(1200,700))
    screen.blit(scaled_bg,(0,0))

    scaled_bg2 = pygame.transform.scale(ai_settings.bg_image2,(1200,700))
    screen.blit(scaled_bg2,(0,0))
    
    # Draw Score to the screen. 
    score_b.show_score()
    
    # Game Ship.   
    ship.blitme()

    # Game Aliens.
    aliens.draw(screen)
   
    # Game Bullets. 
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    # Play_button when game inactive. 
    if not stats.game_active:
        play_button.draw_button()

    # Most recent screen active.   
    pygame.display.flip()

def update_bullets(ai_settings, screen,stats, score_b, ship, aliens, bullets):

    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            
    check_bullet_alien_collisions(ai_settings, stats, score_b, screen, ship, aliens, bullets)
       
def check_bullet_alien_collisions(ai_settings, stats, score_b, screen, ship, aliens, bullets):

    """Respond to bullet-alien collisions."""
    
    # Collisions between Bullets and Aliens.
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
        score_b.prep_score()
        check_high_score(stats, score_b)
        
         
    if len(aliens) == 0 :
        # If the intire fleet is distroyed create a new level.    
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        score_b.prep_level()

def get_number_rows(ai_settings, ship_height, alien_height):
    
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def get_number_aliens_x(ai_settings, alien_width):
    
    """Determine the number of aliens that fit in for a row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings,ship, screen, aliens, alien_number, row_number):
    
    """Drawing Aliens and rows needed to fill the screen."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + 2 * alien_width * alien_number 
    alien.rect.x = alien.x
    alien.rect.y = alien_height + 2 * alien_height * row_number 
    aliens.add(alien)
   
    # Variables for rows and the amount of aliens that needs to fill the screen.
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Rescaling all Aliens to desirable game_size.
    rescale_factor = 2
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            alien.image = pygame.transform.scale(alien.image, (60 * float(rescale_factor),60 * float(rescale_factor)))

def create_fleet(ai_settings, screen, ship, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        # Create the first row of aliens.
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,ship, screen, aliens, alien_number, row_number )
        
def ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets):
   
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0 :
        # Decrement ships_left.
        stats.ships_left -= 1
        
        # Update scoreboard.
        score_b.prep_ships()
        
        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()
        
        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens)

        # Pause.
        sleep(1.5)
       
        # Center ship. 
        ship.center_ship()
       
    else:
        save_highscore(stats, score_b)
        stats.reset_stats()
        stats.game_active = False
        ai_settings.initialize_dynamic_settings()
        ship.center_ship()
        
def update_aliens(ai_settings, stats, score_b, screen, ship, aliens, bullets):
    
    """Update the postions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()
    
    check_aliens_bottom(ai_settings, stats, score_b, screen, ship, aliens, bullets)
    
    # Checks for collision between aliens and ship.
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites(): 
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, stats, score_b, screen, ship, aliens, bullets):
    """Check if any aliens have reached the bottom of the screen."""
    for alien in aliens.sprites():
        if alien.rect.bottom >= 650:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, score_b, screen, ship, aliens, bullets)
            score_b.prep_ships()
            break
            
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
   
def check_high_score(stats, score_b):
    """Check to see if there's a new high score."""
   
    if stats.score > stats.high_score:
        stats.high_score = stats.score 
        score_b.prep_high_score()

def save_highscore(stats, score_b):
            
     with open("high_score.txt", "w") as f:
        if stats.high_score > stats.score:
            f.write(str(stats.high_score))
            
def write_score(stats, score_b):
   
    """ Write highscore when game restarts """
   
    with open("high_score.txt", 'r') as f:
        
        alltime_score = f.read()
       
        if int(alltime_score) > stats.score:
            stats.high_score = int(alltime_score)
            score_b.prep_high_score()
        
        
                

       



           
   
        
    

           

                
