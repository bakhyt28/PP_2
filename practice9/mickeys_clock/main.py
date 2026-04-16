import pygame
from clock import MickeyClock

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

mickey = MickeyClock("images/mickey_hand.png")

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey.draw(screen, (300, 300))

    pygame.display.flip()
    clock.tick(1)

pygame.quit()