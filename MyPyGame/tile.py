import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        """
        Initialize a Tile object.

        Args:
            pos (tuple): The position of the tile.
            groups (tuple): The sprite groups to which the tile belongs.
        """
        super().__init__(groups)
        self.image = pygame.image.load('graphics/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
