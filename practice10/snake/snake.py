import pygame
import random
import sys

# Initialize pygame (start game library)
pygame.init()

# Screen size
WIDTH = 600      
HEIGHT = 400     

# Size of one snake block / food block
CELL = 20        

# Colors in RGB format
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

# Clock to control game speed
clock = pygame.time.Clock()

# Font for score and level text
font = pygame.font.SysFont("Verdana", 20)

# Game speed (controls how fast snake moves)
speed = 5    

# Game level
level = 1      

# Player score
score = 0      

# Snake body (list of coordinates)
# Each tuple is (x, y) position of one segment
snake = [(100, 100), (80, 100), (60, 100)]

# Initial movement direction
direction = "RIGHT"

# Function to create food at random position
def generate_food():
    while True:
        # Random x position (aligned to grid using CELL)
        x = random.randrange(0, WIDTH, CELL)
        
        # Random y position (aligned to grid)
        y = random.randrange(0, HEIGHT, CELL)

        # Food must not appear inside snake body
        if (x, y) not in snake:
            return (x, y)

# Create first food
food = generate_food()

# Main game loop
while True:

    for event in pygame.event.get():
        
        # Exit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard control
        if event.type == pygame.KEYDOWN:
            
            # Change direction but prevent reverse movement
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Get current head position of snake
    head_x, head_y = snake[0]

    # Move head depending on direction
    if direction == "UP":
        head_y -= CELL
    if direction == "DOWN":
        head_y += CELL
    if direction == "LEFT":
        head_x -= CELL
    if direction == "RIGHT":
        head_x += CELL

    # New head position after movement
    new_head = (head_x, head_y)

    # Check collision with walls (game over condition)
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        break  

    # Check collision with itself
    if new_head in snake:
        break 

    # Add new head to snake
    snake.insert(0, new_head)

    # Check if snake eats food
    if new_head == food:
        score += 1
        food = generate_food()  # generate new food

        # Increase level every 3 points
        if score % 3 == 0:
            level += 1
            speed += 1   # increase speed = harder game
    else:
        # Remove last part of snake (movement effect)
        snake.pop()

    # Clear screen
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL, CELL))

    # Draw food
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))

    # Draw score text (top-left)
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 30))

    # Update screen
    pygame.display.update()

    # Control speed of game
    clock.tick(speed)

# Game over screen
screen.fill(RED)

# Text in center of screen
game_over_text = font.render("GAME OVER", True, WHITE)

# Center position calculation
screen.blit(game_over_text, (WIDTH // 2 - 60, HEIGHT // 2 - 20))

# Show final screen
pygame.display.update()

# Pause before closing
pygame.time.delay(2000)

# Exit game
pygame.quit()
sys.exit()