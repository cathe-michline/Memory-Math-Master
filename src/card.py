import pygame
from constants import *

class Card:
    """Creates a card with a given value and position on the screen."""
    def __init__(self, value, x, y):
        self.value = value
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.is_flipped = False
        self.is_matched = False
        self.animating = False
        self.flip_progress = 0.0
        self.flip_speed = 0.05  
        self.pair_value = None
        self.just_flipped = False  

    """Starts the flip animation when the card is clicked."""
    def start_flip(self):
        if not self.is_matched and not self.animating:
            self.animating = True
            self.flip_progress = 0.0
            self.just_flipped = True

    """Updates the card's flip animation frame by frame."""
    def update_animation(self):
        if self.animating:
            self.flip_progress += self.flip_speed
            if self.flip_progress >= 1:
                self.flip_progress = 1
                self.animating = False
                self.is_flipped = not self.is_flipped
                self.just_flipped = False