import pygame
import sys
import math

# Initialize pygame so graphics, mouse and keyboard work
pygame.init()

# Window size (width and height in pixels)
WIDTH, HEIGHT = 800, 600

# Create main window (surface for drawing)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Window title
pygame.display.set_caption("Paint with UI Panel")

# Clock controls program speed (FPS)
clock = pygame.time.Clock()

# Current color (RGB format), default is blue
color = (0, 0, 255)

# Current drawing mode
mode = "draw"

# Brush size (radius for drawing)
radius = 5

# Starting mouse position for shapes
start_pos = None

# True when mouse button is pressed
drawing = False

# Fill background with white color
screen.fill((255, 255, 255))

# Font for UI text
font = pygame.font.SysFont("Arial", 18)

# Function to draw bottom panel
def draw_ui():
    # Gray rectangle at bottom
    # x=0 (left side), y=560 (near bottom)
    # width=800 (full width), height=40 (panel height)
    pygame.draw.rect(screen, (230, 230, 230), (0, 560, 800, 40))

    # Instructions text
    text = "R=Red | G=Green | B=Blue | D=Draw | E=Erase | L=Rect | C=Circle"

    # Convert text into image
    img = font.render(text, True, (0, 0, 0))

    # Draw text on screen
    # x=10 → small margin from left
    # y=570 → inside panel
    screen.blit(img, (10, 570))


# Main loop (runs continuously)
while True:
    for event in pygame.event.get():

        # Close program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Keyboard input
        if event.type == pygame.KEYDOWN:

            # Change color
            if event.key == pygame.K_r:
                color = (255, 0, 0)   # red
            elif event.key == pygame.K_g:
                color = (0, 255, 0)   # green
            elif event.key == pygame.K_b:
                color = (0, 0, 255)   # blue

            # Change mode
            elif event.key == pygame.K_d:
                mode = "draw"   # free drawing
            elif event.key == pygame.K_e:
                mode = "erase"  # eraser
            elif event.key == pygame.K_l:
                mode = "rect"   # rectangle
            elif event.key == pygame.K_c:
                mode = "circle" # circle

        # Mouse button pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

            # Save starting position (x, y coordinates)
            start_pos = event.pos

        # Mouse button released
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            # Save ending position
            end_pos = event.pos

            # Rectangle mode
            if mode == "rect":
                # x, y = top-left corner (minimum values)
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])

                # width = horizontal distance
                w = abs(start_pos[0] - end_pos[0])

                # height = vertical distance
                h = abs(start_pos[1] - end_pos[1])

                # Draw rectangle (outline thickness = 2)
                pygame.draw.rect(screen, color, (x, y, w, h), 2)

            # Circle mode
            elif mode == "circle":
                # dx = difference in x coordinates
                dx = end_pos[0] - start_pos[0]

                # dy = difference in y coordinates
                dy = end_pos[1] - start_pos[1]

                # Radius = distance between two points
                radius_circle = int(math.sqrt(dx*dx + dy*dy))

                # Draw circle from start position
                pygame.draw.circle(screen, color, start_pos, radius_circle, 2)

        # Mouse movement while button is pressed
        if event.type == pygame.MOUSEMOTION and drawing:

            # Free drawing
            if mode == "draw":
                # Draw small circles at cursor position (smooth line)
                pygame.draw.circle(screen, color, event.pos, radius)

            # Eraser
            elif mode == "erase":
                # Draw white circles to remove drawing
                pygame.draw.circle(screen, (255, 255, 255), event.pos, 15)

    # Draw UI panel
    draw_ui()

    # Update screen
    pygame.display.update()

    # Limit speed to 60 FPS
    clock.tick(60)