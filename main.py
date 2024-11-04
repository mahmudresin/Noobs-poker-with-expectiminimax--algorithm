import pygame
import sys
from screens.start_screen import StartScreen
from screens.game_mode import GameMode
from screens.settings_screen import GameSettings
from screens.end_screen import EndScreen
from poker_game import PokerGame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

def main():
    pygame.init()  # Ensure pygame is initialized

    # Initialize default font
    FONT = pygame.font.Font(None, 36)

    # Set up the game screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Poker Game Simulator")

    current_screen = "start_screen"

    # Pass the FONT object to the different screens
    start_screen = StartScreen(FONT)
    game_mode = GameMode(FONT)
    settings_screen = GameSettings(FONT)
    poker_game = PokerGame(FONT)
    end_screen = EndScreen(FONT)

    # Main loop
    while True:
        if current_screen == "start_screen":
            start_screen.display()
            result = start_screen.handle_events()
            if result:
                current_screen = result
        elif current_screen == "game_mode":
            game_mode.display()
            result = game_mode.handle_events()
            if result:
                current_screen = result
        elif current_screen == "settings":
            settings_screen.display()
            result = settings_screen.handle_events()
            if result:
                current_screen = result
        elif current_screen == "play_game":
            current_screen = poker_game.play()
        elif current_screen == "end_screen":
            end_screen.display()
            result = end_screen.handle_events()
            if result:
                current_screen = result

if __name__ == "__main__":
    main()
