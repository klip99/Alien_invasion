import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen, stats):
        
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        # Font settings for scoring information.
        self.text_color = "blue"
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, "purple", "yellow")
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.x =  1100
        self.score_rect.top = 20
        
    def prep_high_score(self):
        
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, "yellow","red")
        
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
        
    def prep_level(self):
        
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, "blue", "green")
        
        # Position of level stats.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.x = 400
        self.level_rect.y = 20
        
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
                ship = Ship(self.ai_settings, self.screen)
                ship.rect.x = 10 + ship_number * ship.rect.width
                ship.rect.y = 10
                self.ships.add(ship)
                
                self.rescale = 1

                ship.image = pygame.transform.scale(ship.image, (60 * float(self.rescale), 60 * float(self.rescale)))
       
    def show_score(self):
    
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        
        # Draw ships.
        self.ships.draw(self.screen)
       
    