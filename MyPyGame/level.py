import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # Sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        # Sprite setup
        self.create_map()
        
    def create_map(self):
        """
        Create the game map based on the WORLD_MAP constant.
        'x' represents obstacles, and 'p' represents the player.
        """
        for row_index, row in enumerate(WORLD_MAP):
            for column_index, column in enumerate(row):
                x = column_index * TILESIZE
                y = row_index * TILESIZE
                if column == 'x':
                    # Create an obstacle tile
                    Tile((x, y), self.visible_sprites, self.obstacles_sprites)
                if column == 'p':
                    # Create a player sprite
                    Player((x, y), self.visible_sprites)

    def run(self):
        """
        Update and draw the game.
        """
        self.visible_sprites.draw(self.display_surface)
