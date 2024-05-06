import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        """
        Initialize a Player object.

        Args:
            pos (tuple): The initial position of the player.
            groups (tuple): The sprite groups to which the player belongs.
        """
        super().__init__(groups)
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
