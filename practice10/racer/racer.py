import pygame, sys
from pygame.locals import *
import random, time

# Initialize pygame
pygame.init()

# FPS (frames per second) and clock to control game speed
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors in RGB format
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Game variables
SPEED = 5      # speed of enemy and coins
SCORE = 0      # how many enemies avoided
COINS = 0      # how many coins collected

# Fonts for text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

# Game over text
game_over = font.render("Game Over", True, BLACK)

# Background image
background = pygame.image.load("Images/AnimatedStreet.png")

# Create game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        
        # Load enemy image
        self.image = pygame.image.load("Images/Enemy.png")
        
        # Rectangle used for position and collision
        self.rect = self.image.get_rect()
        
        # Set initial position
        self.reset()

    def reset(self):
        # Random x position, y = 0 (top of screen)
        # 40 is margin so object stays inside screen
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        
        # Move down (y increases)
        self.rect.move_ip(0, SPEED)
        
        # If enemy goes below screen
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1   # increase score
            self.reset() # respawn at top


# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        
        # Load player image
        self.image = pygame.image.load("Images/Player.png")
        
        # Rectangle for position
        self.rect = self.image.get_rect()

        # Start position (x=160, y=520 → near bottom center)
        self.rect.center = (160, 520)

    def move(self):
        # Get pressed keys
        pressed_keys = pygame.key.get_pressed()
        
        # Move left (x decreases)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        
        # Move right (x increases)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        
        # Load and resize coin image
        original_image = pygame.image.load("Images/Coin.png")
        self.image = pygame.transform.scale(original_image, (40, 40))
        
        # Rectangle for position
        self.rect = self.image.get_rect()
        
        # Set initial position
        self.reset()

    def reset(self):
        # Random position at top
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        # Move down slightly slower than enemy
        self.rect.move_ip(0, SPEED - 2)
        
        # If goes off screen → reset
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()


# Create objects
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Groups for sprites
enemies = pygame.sprite.Group()
enemies.add(E1)

Coins = pygame.sprite.Group()
Coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Custom event to increase speed
INC_SPEED = pygame.USEREVENT + 1

# Trigger event every 1 second (1000 ms)
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:

    for event in pygame.event.get():
        
        # Increase speed over time
        if event.type == INC_SPEED:
            SPEED += 0.005

        # Close game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0, 0))

    # Show score (top-left)
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # Show coins (top-right)
    Coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(Coin_text, (280, 10))

    # Draw and update all objects
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check collision with coins
    collected = pygame.sprite.spritecollide(P1, Coins, False)
    if collected:
        COINS += 1
        for coin in collected:
            coin.reset()  # respawn coin

    # Check collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        
        # Play crash sound
        pygame.mixer.Sound("Sounds/crash.wav").play()
        time.sleep(0.5)

        # Show game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Update screen
    pygame.display.update()

    # Keep FPS stable
    FramePerSec.tick(FPS)