import pygame
from constants import *
from game import Game

class Menu:
    """Sets up the fonts and menu buttons for difficulty selection, how-to-play, and exit."""
    def __init__(self):
        self.font = pygame.font.Font(FONT_NAME, 48)
        self.small_font = pygame.font.Font(FONT_NAME, 28)

        self.buttons = {
            "easy": pygame.Rect(400, 200, 200, 60),
            "medium": pygame.Rect(400, 280, 200, 60),
            "difficult": pygame.Rect(400, 360, 200, 60),
            "how to play": pygame.Rect(400, 440, 200, 50),
            "exit": pygame.Rect(400, 510, 200, 50),
        }

    """Draws the menu title and buttons on the screen."""
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)
        title = self.font.render("Memory Math Master", True, TEXT_COLOR)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 100)))

        for key, rect in self.buttons.items():
            pygame.draw.rect(screen, CARD_FRONT_COLOR, rect, border_radius=8)
            label = self.small_font.render(key.capitalize(), True, TEXT_COLOR)
            screen.blit(label, label.get_rect(center=rect.center))

    """Checks if the user clicked any menu button and returns the selected option."""
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    return key
        return None
