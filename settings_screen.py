import pygame
import sys
from constants import *

class GameSettings:
    def __init__(self,font):
        self.font = font
        self.title = FONT.render("Game Settings", True, WHITE)
        self.start_button = FONT.render("Start Poker Game", True, WHITE)

    def display(self):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        screen.blit(self.title, (SCREEN_WIDTH // 2 - self.title.get_width() // 2, 100))
        screen.blit(self.start_button, (SCREEN_WIDTH // 2 - self.start_button.get_width() // 2, 300))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if SCREEN_WIDTH // 2 - self.start_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.start_button.get_width() // 2 and 300 <= y <= 300 + self.start_button.get_height():
                    return "play_game"
