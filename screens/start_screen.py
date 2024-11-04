import pygame
import sys
from constants import *

class StartScreen:
    def __init__(self, font):
        self.font = font
        self.title = self.font.render("Poker Game Simulator", True, WHITE)
        self.start_button = self.font.render("Start Game", True, WHITE)
        self.quit_button = self.font.render("Quit", True, WHITE)

    def display(self):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        screen.blit(self.title, (SCREEN_WIDTH // 2 - self.title.get_width() // 2, 100))
        screen.blit(self.start_button, (SCREEN_WIDTH // 2 - self.start_button.get_width() // 2, 300))
        screen.blit(self.quit_button, (SCREEN_WIDTH // 2 - self.quit_button.get_width() // 2, 400))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                # Check if the Start Game button is clicked
                if (SCREEN_WIDTH // 2 - self.start_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.start_button.get_width() // 2 and
                        300 <= y <= 300 + self.start_button.get_height()):
                    return "game_mode"
                # Check if the Quit button is clicked
                if (SCREEN_WIDTH // 2 - self.quit_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.quit_button.get_width() // 2 and
                        400 <= y <= 400 + self.quit_button.get_height()):
                    pygame.quit()
                    sys.exit()

