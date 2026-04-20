import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NitrousMusic Ball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
RED = (255, 50, 50)

# Ball properties
ball_radius = 100
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

# Font setup
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball (circle)
    pygame.draw.circle(screen, BLUE, (ball_x, ball_y), ball_radius)

    # Draw the ball's border
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius, 3)

    # Render the text
    text = font.render("nitrousmusic", True, WHITE)
    text_rect = text.get_rect(center=(ball_x, ball_y))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()