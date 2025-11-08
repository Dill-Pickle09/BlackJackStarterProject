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
    global deck
    print("This is Blackjack made in python!")

    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]

    while True:
        showHand(playerHand, dealerHand)
        playerValue = calculateHand(playerHand)

        if playerValue > 21:
            print("You busted! Quite unfortunate to see you lose.")
            return
        
        move = input("Hit or Stand? (h or s) ").lower()

        if move == 'h':
            playerHand.append(deck.pop())
        elif move =='s':
            break
        else:
            print("Invalid choice dum dum, type h or s")

    
    print("\nIt is now the Dealer's turn")
    showHand(playerHand, dealerHand, hideDealer=False)
    
    while calculateHand(dealerHand) < 17:
        dealerHand.append(deck.pop())
        print("Dealer draws: ", dealerHand[-1])

    playerValue = calculateHand(playerHand)
    dealerValue = calculateHand(dealerHand)

    print("\nFinal hands: ")
    showHand(playerHand, dealerHand, hideDealer=False)

    if dealerValue > 21 or playerValue > dealerValue:
        print("You win! Bazinga")
    elif dealerValue == playerValue:
        print("You tied with the dealer lol")
    else:
        print("You lose dummy, Dealer wins")


if __name__ == "__main__":
    blackjackGame()
