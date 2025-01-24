import pygame

class Settings():
       """A class to store all settings for Alien Invasion."""
       def __init__(self):
           """Initialize the game's settings."""
      
           # Screen  settings
           self.screen_width = 1200
           self.screen_height = 700
           self.bg_color = (255,255,255)
           self.bg_image = pygame.image.load("game_images/desert.png")
           self.bg_image2 =pygame.image.load("game_images/planets.png")
           self.ship_speed_factor = 10

           """ Bullets settings """
           self.bullets_speed_factor = 12
           self.bullets_allowed = 20

           # Limits the amount the ships a user has the in the game.
           self.ship_limit = 2
           self.fleet_drop_speed = 10
           # Score added. 
           self.alien_points = 50
           # How quickly the game speeds up
           self.speedup_scale = 1.4
           # How quickly the alien point values increase
           self.score_scale = 1.5
           self.initialize_dynamic_settings()
           
       def initialize_dynamic_settings(self):
             
           """Initialize settings that change throughout the game."""
           self.ship_speed_factor = 10
           self.bullet_speed_factor = 12
           self.alien_speed_factor = 5
           self.fleet_direction = 1
          
       def increase_speed(self):
           
           """Increase speed settings."""
           self.ship_speed_factor *= self.speedup_scale
           self.bullet_speed_factor *= self.speedup_scale
           self.alien_speed_factor *= self.speedup_scale
           self.alien_points *= int(self.score_scale)
           
           
           