import pygame
from constants import *

"""Draws a single card on the screen with its current flip state and value (if flipped)."""
def draw_card(screen, card, font):
    # Simple flip animation based on a width shrink effect
    progress = abs(1 - card.flip_progress * 2) if card.animating else 1
    width = int(CARD_WIDTH * progress)
    if width == 0:
        return

    card_surface = pygame.Surface((width, CARD_HEIGHT))
    color = MATCH_HIGHLIGHT if card.is_matched else (
        CARD_BACK_COLOR if not card.is_flipped else CARD_FRONT_COLOR
    )
    card_surface.fill(color)
    pygame.draw.rect(card_surface, TEXT_COLOR, (0, 0, width, CARD_HEIGHT), 2)

    if card.is_flipped and not card.animating:
        text = font.render(str(card.value), True, TEXT_COLOR)
        text_rect = text.get_rect(center=(width // 2, CARD_HEIGHT // 2))
        card_surface.blit(text, text_rect)

    screen.blit(card_surface, (card.rect.x + (CARD_WIDTH - width) // 2, card.rect.y))

"""Displays the current score and remaining time at the top of the screen."""
def draw_score_timer(screen, score, time_left):
    font = pygame.font.Font(FONT_NAME, 32)
    score_surf = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_surf, (20, 20))
    timer_surf = font.render(f"Time: {time_left}", True, TEXT_COLOR)
    screen.blit(timer_surf, (SCREEN_WIDTH - 160, 20))

"""Displays the number of moves taken by the player."""
def draw_moves(screen, moves):
    font = pygame.font.Font(FONT_NAME, 28)
    move_surf = font.render(f"Moves: {moves}", True, TEXT_COLOR)
    screen.blit(move_surf, (SCREEN_WIDTH // 2 - move_surf.get_width() // 2, 70))