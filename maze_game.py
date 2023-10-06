# Version 3 - Latest

# Import necessary libraries
import pygame
import random

# Initialize Pygame
pygame.init()

# Commit 1
# Constants
WIDTH, HEIGHT = 800, 600  # Screen dimensions
PLAYER_SIZE = 30  # Size of the player character
WHITE = (255, 255, 255)  # Color constants
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SCORE_FONT = pygame.font.Font(None, 36)  # Font for displaying the score
SCORE = 0  # Initial score

# Load sound effects
pickup_sound = pygame.mixer.Sound('ItemPickup.mp3')  # Sound effect for item pickup
background_music = pygame.mixer.Sound('BackgroundMusic.mp3')  # Background music

# Initialize Pygame mixer for audio
pygame.mixer.init()

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game - Version 3")

# Commit 2
# Define the player class with scoring and screen wrapping
class Player:
    def __init__(self):
        self.x = 50  # Initial player position (x-coordinate)
        self.y = 50  # Initial player position (y-coordinate)

    def move(self, dx, dy):
        # Wrap around horizontally and vertically when reaching screen boundaries
        self.x = (self.x + dx) % WIDTH
        self.y = (self.y + dy) % HEIGHT

# Create the player
player = Player()

# Create a list of items to collect with random positions
items = [(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)) for _ in range(10)]

# Game loop
running = True
background_music.play()  # Play background music

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game when the window is closed
    
    # Commit 3
    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-1, 0)  # Move left
    if keys[pygame.K_RIGHT]:
        player.move(1, 0)  # Move right
    if keys[pygame.K_UP]:
        player.move(0, -1)  # Move up
    if keys[pygame.K_DOWN]:
        player.move(0, 1)  # Move down
    
    # Commit 4
    # Check for item collection
    for item in items:
        if pygame.Rect(player.x, player.y, PLAYER_SIZE, PLAYER_SIZE).colliderect(pygame.Rect(item[0], item[1], 20, 20)):
            items.remove(item)
            SCORE += 10  # Increase the score
            pickup_sound.play()  # Play item pickup sound

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player (green square) at its current position
    pygame.draw.rect(screen, GREEN, (player.x, player.y, PLAYER_SIZE, PLAYER_SIZE))

    # Draw the items (blue squares)
    for item in items:
        pygame.draw.rect(screen, BLUE, (item[0], item[1], 20, 20))

    # Display the score on the screen
    score_text = SCORE_FONT.render("Score: " + str(SCORE), True, GREEN)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit Pygame when the game loop exits
pygame.quit()
