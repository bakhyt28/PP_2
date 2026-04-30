import pygame, sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
clock = pygame.time.Clock()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

SPEED = 4

COINS = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

background = pygame.image.load("Images/AnimatedStreet.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/Enemy.png")
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (200, 520)

    def move(self):
        pressed = pygame.key.get_pressed()

        if pressed[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        if pressed[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        img = pygame.image.load("Images/Coin.png")
        self.image = pygame.transform.scale(img, (30, 30))

        self.rect = self.image.get_rect()

        self.value = random.choice([1, 2, 3])

        self.reset()

    def reset(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

        self.value = random.choice([1, 2, 3])

    def move(self):
        self.rect.move_ip(0, SPEED - 2)

        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

P1 = Player()
E1 = Enemy()

coins = pygame.sprite.Group()
for i in range(3):
    coins.add(Coin())

enemies = pygame.sprite.Group(E1)
all_sprites = pygame.sprite.Group(P1, E1, *coins)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    collected = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected:
        COINS += coin.value   
        coin.reset()          

    if COINS >= 40:
        SPEED = 9
    elif COINS >= 20:
        SPEED = 7
    elif COINS >= 10:
        SPEED = 5

    if pygame.sprite.spritecollideany(P1, enemies):
        screen.fill((255, 0, 0))
        text = font_big.render("GAME OVER", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        sys.exit()

    text = font_small.render("Coins: " + str(COINS), True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)