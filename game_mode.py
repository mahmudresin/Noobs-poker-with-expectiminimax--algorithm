import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from main import FONT


class GameMode:
    def __init__(self, font):
        self.font = font
        self.mode_title = self.font.render("Select Game Mode", True, WHITE)
        self.texas_button = self.font.render("Texas Hold'em", True, WHITE)
        self.draw_button = self.font.render("5 Card Draw", True, WHITE)

    def display(self):
        screen = pygame.display.get_surface()
        screen.fill(BLACK)
        screen.blit(self.mode_title, (SCREEN_WIDTH // 2 - self.mode_title.get_width() // 2, 100))
        screen.blit(self.texas_button, (SCREEN_WIDTH // 2 - self.texas_button.get_width() // 2, 300))
        screen.blit(self.draw_button, (SCREEN_WIDTH // 2 - self.draw_button.get_width() // 2, 400))
        pygame.display.update()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if SCREEN_WIDTH // 2 - self.texas_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.texas_button.get_width() // 2 and 300 <= y <= 300 + self.texas_button.get_height():
                    return "settings"
                if SCREEN_WIDTH // 2 - self.draw_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + self.draw_button.get_width() // 2 and 400 <= y <= 400 + self.draw_button.get_height():
                    return "settings"
