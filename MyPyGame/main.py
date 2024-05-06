import pygame, sys
from settings import *
from level import Level

class Game: 
    def __init__(self):
        # Initialize Pygame modules
        pygame.init()
        pygame.mixer.init()
        
        # Create the game window
        self.screen= pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Soul Knight")
        
        # Create a clock object to control the frame rate
        self.clock= pygame.time.Clock()
        
        # Create the game level
        self.level= Level()
        
    def run(self):
        # Main game loop
        while True:
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            # Fill the screen with black
            self.screen.fill('black')
            
            # Run the game level
            self.level.run()
            
            # Update the display
            pygame.display.update()
            
            # Control the frame rate
            self.clock.tick(FPS)
            
if __name__ == '__main__':
    # Create a game object and run the game
    game= Game()
    game.run()
