import pygame
import random
from card import Card
from constants import *
from ui import draw_card, draw_score_timer, draw_moves
from score_manager import ScoreManager

class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.cards = []
        self.selected_cards = []
        self.moves = 0
        self.score = ScoreManager()
        self.time_left = 120
        self.font = pygame.font.Font(FONT_NAME, 36)
        self.feedback_font = pygame.font.Font(FONT_NAME, 40)
        self.small_font = pygame.font.Font(FONT_NAME, 28)
        self.feedback_message = ""
        self.feedback_timer = 0
        self.check_delay = 0
        self.show_congrats = False
        self.congrats_timer = 300
        self.time_up = False
        self.game_over_timer = 300
        self.back_button = pygame.Rect(SCREEN_WIDTH - 160, SCREEN_HEIGHT - 60, 140, 40)
        self.congrats_image = None
        self.game_over_image = None
        self.generate_cards()
        self.timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(self.timer_event, 1000)

    """Creates math expression-answer card pairs based on difficulty level and places them on the screen."""
    def generate_cards(self):
        pairs = set()

        if self.difficulty == "easy":
            while len(pairs) < 6:
                op = random.choice(["+", "-"])
                a, b = random.randint(1, 9), random.randint(1, 9)
                if op == "+":
                    expr = f"{a} + {b}"
                    answer = str(a + b)
                else:
                    a, b = max(a, b), min(a, b)
                    expr = f"{a} - {b}"
                    answer = str(a - b)
                pair = (expr, answer)
                if pair not in pairs:
                    pairs.add(pair)

        elif self.difficulty == "medium":
            while len(pairs) < 8:
                op = random.choice(["+", "-", "x", "÷"])
                if op == "+":
                    a, b = random.randint(10, 20), random.randint(10, 20)
                    expr = f"{a} + {b}"
                    answer = str(a + b)
                elif op == "-":
                    a, b = random.randint(10, 20), random.randint(10, 20)
                    a, b = max(a, b), min(a, b)
                    expr = f"{a} - {b}"
                    answer = str(a - b)
                elif op == "x":
                    a, b = random.randint(1, 5), random.randint(1, 5)
                    expr = f"{a} x {b}"
                    answer = str(a * b)
                else:
                    b = random.randint(1, 5)
                    answer = random.randint(1, 5)
                    a = b * answer
                    expr = f"{a} ÷ {b}"
                    answer = str(answer)
                pair = (expr, answer)
                if pair not in pairs:
                    pairs.add(pair)

        else:
            while len(pairs) < 8:
                op = random.choice(["+", "-", "x", "÷"])
                if op == "+":
                    a, b = random.randint(20, 50), random.randint(20, 50)
                    expr = f"{a} + {b}"
                    answer = str(a + b)
                elif op == "-":
                    a, b = random.randint(20, 50), random.randint(20, 50)
                    a, b = max(a, b), min(a, b)
                    expr = f"{a} - {b}"
                    answer = str(a - b)
                elif op == "x":
                    a, b = random.randint(5, 10), random.randint(5, 10)
                    expr = f"{a} x {b}"
                    answer = str(a * b)
                else:
                    b = random.randint(5, 10)
                    answer = random.randint(2, 10)
                    a = b * answer
                    expr = f"{a} ÷ {b}"
                    answer = str(answer)
                pair = (expr, answer)
                if pair not in pairs:
                    pairs.add(pair)

        card_data = list(pairs) + [(b, a) for (a, b) in pairs]
        random.shuffle(card_data)

        self.cards = []
        start_x = 100
        start_y = 150
        cols = 4
        spacing = CARD_WIDTH + CARD_MARGIN

        for index, (text, match_with) in enumerate(card_data):
            row = index // cols
            col = index % cols
            x = start_x + col * spacing
            y = start_y + row * spacing
            card = Card(text, x, y)
            card.pair_value = match_with
            self.cards.append(card)

        image_folder = os.path.join(os.path.dirname(__file__), "..", "assets", "images")
        image_files = [f for f in os.listdir(image_folder) if f.endswith((".png", ".jpg"))]
        if image_files:
            path = os.path.join(image_folder, random.choice(image_files))
            self.congrats_image = pygame.image.load(path)
            self.congrats_image = pygame.transform.scale(self.congrats_image, (600, 500))

        gameover_folder = os.path.join(os.path.dirname(__file__), "..", "assets", "images", "gameover")
        gameover_files = [f for f in os.listdir(gameover_folder) if f.endswith((".png", ".jpg"))]
        if gameover_files:
            path = os.path.join(gameover_folder, random.choice(gameover_files))
            self.game_over_image = pygame.image.load(path)
            self.game_over_image = pygame.transform.scale(self.game_over_image, (600, 500))

    """Handles player interactions like card clicks, timer updates, and menu navigation."""
    def handle_event(self, event):
        if self.show_congrats or self.time_up or self.check_delay > 0:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.collidepoint(event.pos):
                self.show_congrats = False
                self.time_up = False
                return "menu"

            if len(self.selected_cards) < 2:
                for card in self.cards:
                    if card.rect.collidepoint(event.pos) and not card.is_flipped and not card.animating and not card.is_matched:
                        card.start_flip()
                        self.selected_cards.append(card)
                        break

        elif event.type == self.timer_event:
            if not self.time_up:
                self.time_left = max(0, self.time_left - 1)
                if self.time_left == 0:
                    self.time_up = True
            if self.feedback_timer > 0:
                self.feedback_timer -= 1
                if self.feedback_timer == 0:
                    self.feedback_message = ""

    """Updates card animations, checks for matches, and manages game state (win/lose)."""
    def update(self):
        for card in self.cards:
            card.update_animation()

        if self.time_up:
            self.game_over_timer -= 1
            if self.game_over_timer <= 0:
                return "menu"
            return

        if self.show_congrats:
            self.congrats_timer -= 1
            if self.congrats_timer <= 0:
                return "menu"
            return

        if self.check_delay > 0:
            self.check_delay -= 1
            if self.check_delay == 0:
                self.evaluate_match()

        elif len(self.selected_cards) == 2:
            c1, c2 = self.selected_cards
            if not (c1.animating or c2.animating):
                self.check_delay = 30

        if all(card.is_matched for card in self.cards) and not self.show_congrats:
            self.show_congrats = True

    """Compares two selected cards and updates the score or flips them back if they don’t match."""
    def evaluate_match(self):
        c1, c2 = self.selected_cards
        self.moves += 1
        if (c1.pair_value == c2.value or c2.pair_value == c1.value):
            c1.is_matched = c2.is_matched = True
            self.score.add_match_score(self.moves)
            self.feedback_message = "Correct!"
            self.feedback_timer = 3
        else:
            c1.start_flip()
            c2.start_flip()
        self.selected_cards = []

    """Draws all game elements on the screen including cards, score, timer, and feedback messages."""
    def draw(self, screen):
        screen.fill(BACKGROUND_COLOR)

        if self.time_up:
            over_text = self.feedback_font.render("Time's Up!", True, (200, 0, 0))
            screen.blit(over_text, over_text.get_rect(center=(SCREEN_WIDTH // 2, 100)))
            if self.game_over_image:
                screen.blit(self.game_over_image, self.game_over_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            return

        if self.show_congrats:
            if self.congrats_image:
                screen.blit(self.congrats_image, self.congrats_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))
            return

        for card in self.cards:
            draw_card(screen, card, self.font)

        draw_score_timer(screen, self.score.get_score(), self.time_left)
        draw_moves(screen, self.moves)

        if self.feedback_message:
            feedback = self.feedback_font.render(self.feedback_message, True, (0, 150, 0))
            screen.blit(feedback, feedback.get_rect(center=(SCREEN_WIDTH // 2, 120)))

        back_text = self.small_font.render("Back to Menu", True, TEXT_COLOR)
        screen.blit(back_text, back_text.get_rect(center=self.back_button.center))
