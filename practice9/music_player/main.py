import pygame
from player import MusicPlayer

pygame.init()
screen = pygame.display.set_mode((400, 200))
font = pygame.font.SysFont(None, 36)

player = MusicPlayer()

running = True
while running:
    screen.fill((200, 200, 200))

    text = font.render(f"Track: {player.current}", True, (0, 0, 0))
    screen.blit(text, (50, 80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            if event.key == pygame.K_s:
                player.stop()
            if event.key == pygame.K_n:
                player.next()
            if event.key == pygame.K_b:
                player.prev()
            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()

pygame.quit()