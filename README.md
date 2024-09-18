# BLACKJACK Game

## Overview
This is a simple Blackjack game implemented in Python. The game allows a single player to play against the dealer. The objective is to get a hand value as close to 21 as possible without exceeding it. Aces can count as either 1 or 11 points, and face cards (Jack, Queen, King) count as 10 points.

The game ends when either the player or the dealer wins based on the hand value, with an emphasis on getting exactly 21 (Blackjack) from the first two cards dealt.

## Gameplay
The player is dealt two cards from the deck.
The dealer is also dealt two cards.
The player can choose to:
Stick (end the turn with the current hand)
Hit (draw another card from the deck)
The dealer must keep drawing cards until their hand value is at least 17.
The game compares the hand values of the player and dealer to determine the winner.
Blackjack Rule
In this version, Blackjack is only considered when the player gets 21 with the first two cards (an Ace and any 10-point card like a King, Queen, Jack, or 10).

## How to Run
1. Clone the Repository: Clone the repository to your local machine.
2. Run the Application:
- Windows: ``python main.py``
- Mac: ``python3 main.py``
3. Follow the on-screen prompts to play the game.

### Future Improvements
- Images: Add visual representations of the cards to enhance the gameplay experience. This can be done using external libraries like PIL or pygame to render card images.
- Features: Expand the game with more features such as multiple players, betting options, and better handling of edge cases like ties and insurance in Blackjack.
### Current Limitations
The game is text-based without graphical elements (card images).
The Blackjack condition isn't restricted to the player getting exactly 21 with the first two cards only.
Enjoy the game!