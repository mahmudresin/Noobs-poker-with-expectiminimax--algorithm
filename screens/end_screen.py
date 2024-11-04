import pygame
import sys
from constants import *

class EndScreen:
    def __init__(self,font):
        self.font = font
        self.end_message = FONT.render("Game Over. Play Again?", True, WHITE)
        self.yes_button = FONT.render("Yes", True, WHITE)
        self.no_button = FONT.render("No", True, WHITE)

    def display(self):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        screen.blit(self.end_message, (SCREEN_WIDTH // 2 - self.end_message.get_width() // 2, 200))
        screen.blit(self.yes_button, (SCREEN_WIDTH // 2 - self.yes_button.get_width() // 2, 300))
        screen.blit(self.no_button, (SCREEN_WIDTH // 2 - self.no_button.get_width() // 2, 400))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if SCREEN_WIDTH // 2 - self.yes_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.yes_button.get_width() // 2 and 300 <= y <= 300 + self.yes_button.get_height():
                    return "start_screen"
                if SCREEN_WIDTH // 2 - self.no_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.no_button.get_width() // 2 and 400 <= y <= 400 + self.no_button.get_height():
                    pygame.quit()
                    sys.exit()
