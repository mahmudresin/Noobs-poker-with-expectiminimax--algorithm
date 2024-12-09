
 Noobs Poker - README
Introduction
**Noobs Poker** is a graphical poker game built using Python's `pygame` library. It provides a fun and interactive experience with multiple rounds of poker involving a player and three computer-controlled opponents. The game showcases classic poker gameplay, where players can select and replace cards in their hands, while AI opponents make decisions using an Expectiminimax algorithm.

Features
- A simple poker game with 4 players (1 human player and 3 AI opponents).
- AI decision-making using Expectiminimax for card replacements.
- Custom fonts and graphical interface with card images and a dynamic scoreboard.
- Responsive user input for starting the game, selecting cards, and progressing through rounds.

 Installation
Prerequisites
1. Python 3.x
2. Pygame library (`pip install pygame`)
3. Ensure the necessary image assets (cards, background, and font files) are present in the appropriate folders.

 File Structure
- `main.py`: Main game logic.
- `PokerModel.py`: Contains the game logic for poker hands, deck, and AI decision-making.
- `img/`: Contains image files for the background, card back, and card faces (e.g., `2H.png`, `3S.png` for the 2 of Hearts, 3 of Spades, etc.).
- `font/`: Contains custom font files (`CoffeeTin.ttf`, `IndianPoker.ttf`).

How to Run
1. Clone or download the repository.
2. Make sure you have the `img` and `font` directories with the necessary assets.
3. Run the game:
   ```bash
   python main.py
   ```

 Gameplay
1. **Startup Screen**: 
   - The game begins with a startup screen displaying "Noobs Poker" and a "Start" button. Click the "Start" button to begin.
   
2. **Player's Turn**:
   - Once the game starts, you'll see your hand of 5 cards displayed on the screen. 
   - You can click on a card to select it for replacement (card will flip over to indicate selection).
   - After selecting cards, click the "Replace" button to exchange selected cards for new ones from the deck.

3. **AI's Turn**:
   - The computer players will also replace their cards based on an AI algorithm.

4. **Results**:
   - After two rounds, the game will display the results of the hand and show each player's final hand and scores.
   - You can then start a new game by clicking "New Game."

AI Behavior
The computer players use an **Expectiminimax** algorithm for decision-making. This algorithm simulates possible outcomes for card replacements and chooses the best hand based on expected values, considering both maximizing its score and minimizing losses.

 Controls
- **Mouse Click**: 
  - Click on cards to select/deselect them.
  - Click on buttons like "Start" and "Replace" to progress through the game.
  
 Assets
- **Card Images**: PNG images for all card faces and the card back.
- **Background**: A background image for the poker table.
- **Fonts**: Custom fonts for game text.

 Dependencies
- **Pygame**: Used for rendering the game graphics and handling user input.

To install pygame:
```bash
pip install pygame
```

 Future Improvements
- Add support for different poker variants.
- Implement more advanced AI strategies.
- Include additional game sounds and animations.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.



Enjoy the game, and happy playing!
