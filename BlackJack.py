## Black Jack game ##
# OBS: A simple BlackJack game can be played, no splitting, doubling can be done

# 1) Importing

import random
import time

# 2) Classes

class Card:
    """
    Class used to create a card
    """
    def __init__(self, value, color):
        self.value = value
        self.color = color
        self.face_up = False

    def __str__(self):
        return f'{self.value} of {self.color}'

    def get_value(self):
        return self.value

    def get_color(self):
        return self.color

class Deck(Card):
    """
    Class used to create a Deck of cards
    """
    def __init__(self):
        self.deck = []

        for color in ('Clubs', 'Diamonds', 'Hearts', 'Spades'):
            for value in (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'):
                self.deck.append(Card(value, color))

    def __str__(self):
        for card in self.deck:
            return f'{card.get_value()} of {card.get_color()}'

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)

class Player(Deck, Card):
    """
    Class used to create the players
    """
    def __init__(self):
        super().__init__()
        self.hand = []

    def draw_hand(self, deck):
        self.hand.append(deck.draw_card())

    def flip_card(self):
        self.hand[-1].face_up = True

    def show_hand(self):
        for card in self.hand:
            print(card)

    def get_count(self):
        self.count = 0

        for card in self.hand:
            if card.get_value() in ('J', 'Q', 'K', 'A'):
                self.count += 10

            elif card.get_value() in (2, 3, 4, 5, 6, 7, 8, 9, 10):
                self.count += card.get_value()

        return self.count

    def print_hand(self):
        for i in range(0, len(self.hand)):
            if self.hand[i].face_up == True:
                print(self.hand[i])
            elif self.hand[i].face_up == False:
                print('Face down card')
        print('')

# 3) Main code
game_over = False
deck = Deck()  # Create deck
deck.shuffle()  # Shuffle deck
player = Player()   # Create player
dealer = Player()   # Create dealer

# First round
print('=-' * 30)
print('              Welcome to BlackJack !')
print('=-' * 30)
player.draw_hand(deck)  # Player draws one card from deck
player.flip_card()  # Player flips one card
player.draw_hand(deck)  # Player draws one card from deck
player.flip_card()  # Player flips one card
dealer.draw_hand(deck)  # Dealer draws one card from deck
dealer.flip_card()  # Dealer flips one card
dealer.draw_hand(deck)  # Dealer draws one card from deck
time.sleep(3)
print('Dealer hand')
print('-' * 15)
dealer.print_hand()  # Show Dealer hand
print('Player hand')
print('-' * 15)
player.print_hand()  # Show Player hand

# Next rounds
while True:
    time.sleep(3)
    print('-=' * 20)
    move = str(input('Player 1, hit or stay (H/S): ')).strip().upper()[0]

    if move == 'H':
        player.draw_hand(deck)  # Player draws one card from deck
        player.flip_card()  # Player flips one card
        time.sleep(3)
        print('-=' * 20)
        print('Dealer hand')
        print('-' * 15)
        dealer.print_hand()  # Show Dealer hand
        print('Player hand')
        print('-' * 15)
        player.print_hand()  # Show Player hand

        # win check
        if player.get_count() <= 21:
            continue

        elif player.get_count() > 21:
            game_over = True
            print('You are over 21, dealer wins !!')

        if game_over == True:
            break

    elif move == 'S':
        dealer.flip_card()  # Dealer flips one card
        time.sleep(3)
        print('-=' * 20)
        print('Dealer hand')
        print('-' * 15)
        dealer.print_hand()  # Show Dealer hand
        print('Player hand')
        print('-' * 15)
        player.print_hand()  # Show Player hand

        # win check
        if dealer.get_count() > player.get_count() and dealer.get_count() <= 21:
            print('Dealer win !!')
            game_over = True
            break

        else:
            while dealer.get_count() <= player.get_count():
                dealer.draw_hand(deck)  # Dealer draws one card from deck
                dealer.flip_card()  # Dealer flips one card
                time.sleep(3)
                print('-=' * 20)
                print('Dealer hand')
                print('-' * 15)
                dealer.print_hand()  # Show Dealer hand
                print('Player hand')
                print('-' * 15)
                player.print_hand()  # Show Player hand

                # win check
                if dealer.get_count() > player.get_count() and dealer.get_count() <= 21:
                    print('Dealer win !!')
                    game_over = True
                    break

                elif dealer.get_count() > 21:
                    print('Dealer is over 21, you win !!')
                    game_over = True
                    break

            if game_over == True:
                break















