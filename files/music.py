import pygame
from pygame.locals import *

class Play:
    def play_movement():
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/slime_bounce_02.wav'))

    def play_forest():
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('assets/sounds/forest.wav'), -1)

    def play_jump():
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('assets/sounds/largo_bounce_02.wav'))

    def play_chomp():
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('assets/sounds/slime_chomp_03.wav'))