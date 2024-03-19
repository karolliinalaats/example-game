import pygame

class player(pygame.sprite.Sprite):
    """Class for player object"""
    
    
    def __init__(self, screen):
        """initialize player"""
        super(Player, self).__ninit__()
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.player = pygame.Surface((75,25))
        self.player.fill((255, 0, 0))
        self.rect = self.player.get_rect()
        
        def blit_me(self):
            self.screen.blitt(self.player, self.rect)