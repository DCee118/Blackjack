import random

# Suits and Ranks for the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Card values in Blackjack
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Card class to represent each card with rank and suit
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}" 

    @property
    def value(self):
        return values[self.rank]

# Deck class to represent a full deck of cards
class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(self.cards) 

    def draw(self):
        return self.cards.pop()  # Draw a card from the deck

def calculate_hand(hand):
    value = sum(card.value for card in hand)
    aces = sum(1 for card in hand if card.rank == 'Ace')
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def player_hand(deck):
    hand = [deck.draw(), deck.draw()]
    
    while True:
        value = calculate_hand(hand)
        print(f"Your hand: {hand}, value: {value}") 

        if value == 21:
            print("Blackjack!")
            return value
        if value > 21:
            print("Bust!")
            return value    

        hit_or_stick = input('Press 1 to Stick\nPress 2 to Hit\n')
        if hit_or_stick == '1':
            print(f"Final hand: {hand}, value: {value}")
            return value 
        elif hit_or_stick == '2':
            hand.append(deck.draw())
        else:
            print("Invalid input, please enter 1 to Stick or 2 to Hit.")


def is_blackjack(hand):
    return len(hand) == 2 and (
        (hand[0].rank == 'Ace' and hand[1].value == 10) or
        (hand[1].rank == 'Ace' and hand[0].value == 10)
    )
    
def dealer_hand(deck):
    hand = [deck.draw(), deck.draw()]
    print(f"Dealer's initial hand: {hand}")

    # Dealer must hit until the hand is at least 17
    while calculate_hand(hand) < 17:
        hand.append(deck.draw())
        print(f"Dealer draws: {hand}")
    
    return calculate_hand(hand)

def main():
    deck = Deck() 
    player = player_hand(deck)
    dealer = dealer_hand(deck)

    print(f"Player hand value: {player}")
    print(f"Dealer hand value: {dealer}")

    if player > 21:
        print('BUST')
    elif player == 21:
        print('Blackjack!')
    elif dealer > 21:
        print('Dealer BUST, You Win!')
    elif player > dealer:
        print('You Win!')
    elif player == dealer:
        print('Push.')
    else:
        print('Dealer Wins.')


if __name__ == "__main__":
    main()