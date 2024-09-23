import time
from itertools import product
from random import shuffle

# define suits and ranks using Unicode symbols for suits
SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]  # Clubs, Hearts, Diamonds, Spades
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# card class to represent each card with rank and suit
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    @property
    def value(self):
        return 10 if self.rank in ['J', 'Q', 'K'] else 11 if self.rank == 'A' else int(self.rank)

# deck class to represent a full deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank, suit in product(RANKS, SUITS)]
        shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

# calcultes the value of the hand and changes the value of the ace depending on if the hand is over 21.
def calculate_hand_value(hand):
    value = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'A')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

# visual representation of the cards plus the value.
def display_hand(hand):
    visual_card = " ".join(f"{card.rank}{card.suit}" for card in hand)
    value = calculate_hand_value(hand)
    return f"{visual_card} Value: {value}"

# dealer dealing himself and the player the first two cards each
def deal_initial_cards(deck, player_hand, dealer_hand):
    print('Dealer deals you one card.')
    player_hand.append(deck.draw())  
    print(display_hand(player_hand))    
    time.sleep(1)
    
    print('Dealer deals himself one card.')
    dealer_hand.append(deck.draw())  
    print(display_hand(dealer_hand))    
    time.sleep(1)
    
    print('Dealer deals you your second card.')
    player_hand.append(deck.draw())  
    print(display_hand(player_hand))    
    time.sleep(1)
    
    print('Dealer deals himself a second card face down.')
    dealer_hand.append(deck.draw())     
    time.sleep(1)
    
# handle the player's turn: the player can either stick or hit. 
def player_turn(deck, hand):
    while True:
        value = calculate_hand_value(hand)

        if value == 21:
            print("You have 21!")
            return value
        elif value > 21:
            print("Bust! You exceeded 21.")
            return value

        action = input("Press 1 to Stick or 2 to Hit: ").strip()
        if action == '1':
            print(f"You chose to Stick with {value}.")
            return value
        elif action == '2':
            hand.append(deck.draw())  
            print("You drew a card.")
            print(display_hand(hand))
            time.sleep(1)
        else:
            print("Invalid input. Please enter 1 to Stick or 2 to Hit.")

# handle the dealer's turn: the dealer must hit until their hand value is 17 or higher.
def dealer_turn(deck, hand):
    print("\nDealer's turn:")
    time.sleep(1)  
    print("Dealer flips over second card.")
    time.sleep(1) 
    print(display_hand(hand))
    while calculate_hand_value(hand) < 17:
        hand.append(deck.draw())  
        print("Dealer draws a card:")
        time.sleep(1)
        print(display_hand(hand))
        time.sleep(2)  

    dealer_value = calculate_hand_value(hand)
    return dealer_value

# if the hand is blackjack. 
def is_blackjack(hand):
    return len(hand) == 2 and (
        (hand[0].rank == 'A' and hand[1].value == 10) or
        (hand[1].rank == 'A' and hand[0].value == 10)
    )

# determine win, lose or draw
def game_result(player_hand, dealer_hand, deck):
    player_blackjack = is_blackjack(player_hand)
    dealer_blackjack = is_blackjack(dealer_hand)

    # check for blackjack scenarios
    if player_blackjack and dealer_blackjack:
        return "Both you and the dealer have Blackjack! It's a push!"
    elif player_blackjack:
        return "Blackjack! You win!"
    elif dealer_blackjack:
        return "Dealer has Blackjack! Dealer wins!"

    # if no blackjack, proceed with player's turn
    print("\nPlayer's turn:")
    player_value = player_turn(deck, player_hand)

    # check if the player busts
    if player_value > 21:
        return "Dealer wins!"
    else:
        # proceed with the dealer's turn
        dealer_value = dealer_turn(deck, dealer_hand)
        print("\nDealer's final hand:")
        print(display_hand(dealer_hand))

        # final result
        if dealer_value > 21:
            return "Dealer busts! You win!"
        elif player_value > dealer_value:
            return f"You win! Your {player_value} beats Dealer's {dealer_value}."
        elif player_value < dealer_value:
            return f"Dealer wins with {dealer_value}."
        else:
            return "Push."
                  
def main():
    play_again = True

    while play_again:
        deck = Deck()
        player_hand = []
        dealer_hand = []

        deal_initial_cards(deck, player_hand, dealer_hand)

        print(game_result(player_hand, dealer_hand, deck))

        play_again = input('Play again? (Yes or No): ').strip().lower() == 'yes'

    print("Thanks for playing!")

if __name__ == "__main__":
    main()