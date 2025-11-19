import pygame
import sys
from menu import Menu
from game import Game
from constants import *

"""Starts the game, runs the main loop, and switches between the menu and gameplay."""
def main():
    """
    Initializes the game, handles the main loop, and manages transitions
    between the menu, game, and 'How to Play' screens.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Memory Math Master")
    clock = pygame.time.Clock()

    menu = Menu()
    game = None
    current_state = "menu"

    """Displays instructions on how to play the game and waits for the user to return to the menu."""
    def show_how_to_play():
        """
        Displays the 'How to Play' instructions screen and waits for user input
        to return to the main menu.
        """
        title_font = pygame.font.Font(FONT_NAME, 36)
        line_font = pygame.font.Font(FONT_NAME, 24)

        title = title_font.render("How to Play", True, TEXT_COLOR)
        
        instructions = [
            "Your goal is to match math expressions with their correct answers.",
            "",
            "Difficulty Levels:",
            "  • Easy:        +, -   (Numbers up to 9)",
            "  • Medium:      +, -, ×, ÷   (Answers up to 20, Factors 1–5)",
            "  • Difficult:   +, -, ×, ÷   (Answers up to 50, Factors 5–10)",
            "",
            "Gameplay Instructions:",
            "  • Click on two cards to flip them.",
            "  • If they match, they stay revealed.",
            "  • Match all pairs before time runs out!",
            "",
            "Click anywhere to return to the main menu."
        ]

        screen.fill(BACKGROUND_COLOR)
        screen.blit(title, title.get_rect(center=(SCREEN_WIDTH // 2, 60)))

        y = 120
        for line in instructions:
            rendered = line_font.render(line, True, TEXT_COLOR)
            screen.blit(rendered, (60, y))
            y += 35

        pygame.display.flip()

        # Wait for user to click to return to the main menu
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    while True:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if current_state == "menu":
                result = menu.handle_events(event)
                if result == "exit":
                    pygame.quit()
                    sys.exit()
                elif result == "how to play":
                    show_how_to_play()
                elif result in ["easy", "medium", "difficult"]:
                    game = Game(result)
                    current_state = "game"

            elif current_state == "game":
                result = game.handle_event(event)
                if result == "menu":
                    current_state = "menu"
                    game = None

        if current_state == "menu":
            menu.draw(screen)
        elif current_state == "game":
            result = game.update()
            if result == "menu":
                current_state = "menu"
                game = None
            else:
                game.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()