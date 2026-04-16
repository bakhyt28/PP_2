import pygame
import datetime

class MickeyClock:
    def __init__(self, hand_image):
        self.hand = pygame.image.load(hand_image)
        self.hand = pygame.transform.scale(self.hand, (150, 20))

    def get_time_angles(self):
        now = datetime.datetime.now()
        seconds = now.second
        minutes = now.minute

        return seconds * 6, minutes * 6

    def draw(self, screen, center):
        sec_angle, min_angle = self.get_time_angles()

        sec_hand = pygame.transform.rotate(self.hand, -sec_angle)
        screen.blit(sec_hand, sec_hand.get_rect(center=center))

        min_hand = pygame.transform.rotate(self.hand, -min_angle)
        screen.blit(min_hand, min_hand.get_rect(center=center))