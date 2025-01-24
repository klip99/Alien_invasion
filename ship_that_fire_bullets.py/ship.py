import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        
        super(Ship, self).__init__()
        
        """Initialize the ship and set its starting position."""
        self.screen = screen
        # Load the ship image and get its rect.
        self.image = pygame.image.load("game_images/my_battleship.png")
        self.scale = pygame.transform.scale(self.image, (100,100))
        self.rect = self.scale.get_rect()
        self.screen_rect = screen.get_rect()

        # Initialize ships position.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Moving speed.
        self.speed = ai_settings.ship_speed_factor
        
        # Movement flag
        self.moving_right = False 
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
    # Updates movement state.   
    def update(self):
        
        if self.moving_right and self.rect.right < 1200:
            self.rect.x += self.speed
              
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.speed
            
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.speed
           
        if self.moving_down and self.rect.bottom < 1000:
            self.rect.y += self.speed
           
    # Draws ship to the screen.
    def blitme(self):
        
        """Draw the ship at its current location."""
        self.screen.blit(self.scale, self.rect)
        
    def center_ship(self):
            
        """ X positions """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom