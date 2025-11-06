#Black Jack Python Project

import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
deck = [(rank, suit) for rank in ranks for suit in suits]

random.shuffle(deck)

# just to check if deck has right number of cards
# print("Deck is ready with", len(deck), "cards.")

playerHand = [deck.pop(), deck.pop()]
dealerHand = [deck.pop(), deck.pop()]

print("Your cards: ", playerHand)
print("Here is one of the dealer's cards: ", dealerHand[0])

def calculateHand(hand):
    value = 0
    aces = 0
    for rank, suit in hand:
        if rank in ['jack', 'queen', 'king']:
            value += 10
        elif rank == 'ace':
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value


def showHand(playerHand, dealerHand, hideDealer=True):
    print("Your hand: ", playerHand, "\nValue: ", calculateHand(playerHand))
    if hideDealer:
        print("Dealer shows: ", dealerHand[0])
    else:
        print("Dealer hand: ", dealerHand, "\nValue: ", calculateHand(dealerHand))


def blackjackGame():
    