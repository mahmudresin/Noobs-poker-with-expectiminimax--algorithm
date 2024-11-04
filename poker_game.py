import pygame
from constants import *

class PokerGame:
    def __init__(self):
        self.running = True

    def play(self):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        game_text = FONT.render("Playing Poker...", True, WHITE)
        screen.blit(game_text, (SCREEN_WIDTH // 2 - game_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_text.get_height() // 2))
        pygame.display.update()
        pygame.time.wait(2000)  # Simulate game play duration
        return "end_screen"
