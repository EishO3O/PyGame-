import pygame

# Initialize Pygame
pygame.init()

# Define a font for debug text
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    """
    Display debug information on the screen.

    Args:
        info (str): The debug information to display.
        y (int, optional): The vertical position of the debug text. Default is 10.
        x (int, optional): The horizontal position of the debug text. Default is 10.
    """
    # Get the display surface
    display_surface = pygame.display.get_surface()

    # Render the debug text
    debug_surf = font.render(str(info), True, 'White')
    
    # Get the rectangle for the debug text
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    
    # Draw a black rectangle behind the debug text
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    
    # Blit the debug text onto the display surface
    display_surface.blit(debug_surf, debug_rect)
