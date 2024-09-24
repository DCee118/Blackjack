import time
from itertools import product
from random import shuffle

# Define suits and ranks using Unicode symbols for suits
SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]  # Clubs, Hearts, Diamonds, Spades
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Card class to represent each card with rank and suit
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    @property
    def value(self):
        return 10 if self.rank in ['J', 'Q', 'K'] else 11 if self.rank == 'A' else int(self.rank)

# Deck class to represent a full deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in product(RANKS, SUITS)]
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

# Calculates the value of the hand and adjusts for aces
def calculate_hand_value(hand):
    value = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# Display a hand with formatted cards and value
def display_hand(hand):
    visual_cards = " | ".join(f"{card.rank}{card.suit}" for card in hand)
    value = calculate_hand_value(hand)
    return f"\nhand: {visual_cards} | Value: {value}"

# Deal initial cards 
def deal_initial_cards(deck, player_hand, dealer_hand):
    print('\nDealing cards...\n')
    time.sleep(1)

    print('Dealer deals you one card:')
    player_hand.append(deck.draw())
    print(display_hand(player_hand))
    time.sleep(1)

    print('\nDealer deals himself one card:')
    dealer_hand.append(deck.draw())
    print(display_hand(dealer_hand))
    time.sleep(1)

    print('\nDealer deals you your second card:')
    player_hand.append(deck.draw())
    print(display_hand(player_hand))
    time.sleep(1)

    print('\nDealer deals himself a second card face down.')
    dealer_hand.append(deck.draw())
    time.sleep(1)

# Handle the player's turn with improved prompts and formatting
def player_turn(deck, hand):
    print("\n" + "-" * 40 + "\n" + " " * 10 + "PLAYER'S TURN" + "\n" + "-" * 40)
    while True:
        value = calculate_hand_value(hand)
        print(display_hand(hand))

        if value == 21:
            print("You have 21!")
            return value
        elif value > 21:
            print("Bust! You exceeded 21.")
            return value

        action = input("\nPress 1 to Stick or 2 to Hit: ").strip()
        if action == '1':
            print(f"\nYou chose to Stick with {value}.")
            return value
        elif action == '2':
            hand.append(deck.draw())
            print("\nYou drew a card...")
            time.sleep(1)
        else:
            print("\nInvalid input. Please enter 1 to Stick or 2 to Hit.")

# Handle the dealer's turn with formatting
def dealer_turn(deck, hand):
    print("\n" + "-" * 40 + "\n" + " " * 10 + "DEALER'S TURN" + "\n" + "-" * 40)
    time.sleep(1)
    print("Dealer flips over the second card.")
    time.sleep(1)
    print(display_hand(hand))
    
    while calculate_hand_value(hand) < 17:
        hand.append(deck.draw())
        print("\nDealer draws a card...")
        time.sleep(1)
        print(display_hand(hand))
        time.sleep(1)

    dealer_value = calculate_hand_value(hand)
    return dealer_value

# Check if the hand is Blackjack
def is_blackjack(hand):
    return len(hand) == 2 and (
        (hand[0].rank == 'A' and hand[1].value == 10) or
        (hand[1].rank == 'A' and hand[0].value == 10)
    )

# Determine the result 
def game_result(player_hand, dealer_hand, deck):
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    # Check for Blackjack scenarios
    if player_blackjack and dealer_blackjack:
        return "\nBoth you and the dealer have Blackjack! It's a push!"
    elif player_blackjack:
        return "\nBlackjack! You win!"
    elif dealer_blackjack:
        return "\nDealer has Blackjack! Dealer wins!"

    # If no Blackjack, proceed with player's turn
    player_value = player_turn(deck, player_hand)

    # Check if the player busts
    if player_value > 21:
        return "\nDealer wins!"
    else:
        # Proceed with the dealer's turn
        dealer_value = dealer_turn(deck, dealer_hand)
        print("\nDealer's final hand:")
        print(display_hand(dealer_hand))

        # Final result
        if dealer_value > 21:
            return "\nDealer busts! You win!"
        elif player_value > dealer_value:
            return f"\nYou win! Your {player_value} beats Dealer's {dealer_value}."
        elif player_value < dealer_value:
            return f"\nDealer wins with {dealer_value}."
        else:
            return "\nIt's a push."

# Main game loop 
def main():
    play_again = True

    while play_again:
        print("\n" + "="*40 + "\n" + " " * 15 + "BLACKJACK" + "\n" + "="*40)
        time.sleep(1)
        
        deck = Deck()
        player_hand = []
        dealer_hand = []

        deal_initial_cards(deck, player_hand, dealer_hand)

        print(game_result(player_hand, dealer_hand, deck))

        play_again = input('\nWould you like to play again? (Yes or No): ').strip().lower() == 'yes'
        if play_again:
            print("\nStarting a new round...\n")
            time.sleep(1)
        else:
            print("\nThanks for playing!")

if __name__ == "__main__":
    main()
