import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.image = pygame.image.load("game_images/darksun.png")
        self.scale = pygame.transform.scale(self.image, (50,50))
        self.rect = self.scale.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each bullets at the top of the shop
        self.rect.topright = ship.rect.topright
        self.rect.topleft = ship.rect.topleft

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullets_speed_factor
        
        # Set flag for bullet movement.
        self.moving_up = False
    
    # updates bullets movement and direction.
    def update(self):
        
        """Move the bullet up the screen."""
        self.y -= self.speed_factor
        self.rect.y = self.y
       
    def draw_bullet(self):
        
        """Draw the bullet to the screen."""
        self.screen.blit(self.scale, self.rect)