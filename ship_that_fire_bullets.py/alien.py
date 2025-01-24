import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
       """A class to represent a single alien in the fleet."""

       def __init__(self, ai_settings, screen):
           
           """Initialize the alien and set its starting position."""
           super(Alien, self).__init__()

           self.screen = screen
           self.ai_settings = ai_settings

           # Load the alien image and set its rect attribute.
           self.image = pygame.image.load("game_images/enemy_ship.png")
           self.rescale = pygame.transform.scale(self.image, (60,60))
           self.rect = self.rescale.get_rect()
           self.screen_rect = screen.get_rect()

           # Start each new alien near the top left of the screen.
           self.rect.x = self.rect.x
           self.rect.y = self.rect.y

           # Store the alien's exact position.
           self.x = float(self.rect.x)

       def update(self):

           """Move the alien right or left."""
           # Right movement.
           self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
           self.rect.x = self.x

       def check_edges(self):
           
            """Return True if alien is at edge of screen."""
            if self.rect.right >= 1150:
                return True
            elif self.rect.left <= 0:
                return True

                
                
           

                

