import tkinter as tk
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

def calculateHand(hand):
    value = 0
    aces = 0
    for rank, suit in hand:
        if rank in ['jack', 'queen', 'king']:
            value +=10
        elif rank == 'ace':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

root = tk.Tk()
root.title("Blackjack in Python")
root.geometry("700x500")
root.config(bg="#006400")

deck = []
playerHand = []
dealerHand = []

statusLabel = tk.Label(root, text="Welcome to Blackjack!", font=("Arial", 20), bg="#006400", fg="white")
statusLabel.pack(pady=20)

playerLabel = tk.Label(root, text="", font=("Arial", 14), bg="#006400", fg="white")
playerLabel.pack(pady=10)

dealerLabel = tk.Label(root, text="", font=("Arial", 14), bg="#006400", fg="white")
dealerLabel.pack(pady=10)

buttonFrame = tk.Frame(root, bg="#006400")
buttonFrame.pack(pady=20)

def newDeck():
    global deck
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

def dealCard(hand):
    if deck:
        hand.append(deck.pop())

def updateLabels():
    playerText = ', '.join([f"{r} of {s}" for r, s in playerHand])
    dealerText = ', '.join([f"{r} of {s}" for r, s in dealerHand])
    playerLabel.config(text=f"Your Hand: {playerText} (Value: {calculateHand(playerHand)})")
    dealerLabel.config(text=f"Dealer Hand: {dealerText} (Value: {calculateHand(dealerHand)})")

def startGame():
    global playerHand, dealerHand
    newDeck()
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]
    updateLabels()
    statusLabel.config(text="Game has started: hit or stand?")
    hitButton.config(state="normal")
    standButton.config(state="normal")

def hit():
    dealCard(playerHand)
    updateLabels()
    if calculateHand(playerHand) > 21:
        statusLabel.config(text="You busted, dealer wins")
        hitButton.config(state="disabled")
        standButton.config(state="disabled")

def stand():
    while calculateHand(dealerHand) < 17:
        dealCard(dealerHand)
    updateLabels()
    playerValue = calculateHand(playerHand)
    dealerValue = calculateHand(dealerHand)

    if dealerValue > 21 or playerValue > dealerValue:
        result = "You win!"
    elif dealerValue == playerValue:
        result = "You tied with the dealer"
    else:
        result = "Dealer wins, you lose lol"

    statusLabel.config(text=result)
    hitButton.config(state="disabled")
    standButton.config(state="disabled")


hitButton = tk.Button(buttonFrame, text="Hit", font=("Arial", 14), bg="white", command=hit, state="disabled")
hitButton.grid(row=0, column=10, padx=10)

standButton = tk.Button(buttonFrame, text="Stand", font=("Arial", 14), bg="white", command=stand, state="disabled")
standButton.grid(row=0, column=1, padx=10)

startButton = tk.Button(buttonFrame, text="Start Game", font=("Arial", 14), bg="yellow", command=startGame)
startButton.grid(row=0, column=2, padx=10)

root.mainloop()