import pygame

class Ship():

    def __init__(self,ai_settings, screen):
        """Inicilize the ship and set its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings
        #Load the ship image and get it rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom

        #Store a decimal value for the ship´s center
        self.center = float(self.rect.centerx)

        #movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor + 1
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        #self.rect.centerx = self.center
    
    def blitme(self):
        """Draw the ship in it current position"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

