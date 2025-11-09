import tkinter as tk
from PIL import Image, ImageTk
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

'''
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

'''

def newDeck():
    global deck
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

def dealCard(hand):
    if deck:
        hand.append(deck.pop())

''' (Originally used for tkinter text based version)
def updateLabels():
    playerText = ', '.join([f"{r} of {s}" for r, s in playerHand])
    dealerText = ', '.join([f"{r} of {s}" for r, s in dealerHand])
    playerLabel.config(text=f"Your Hand: {playerText} (Value: {calculateHand(playerHand)})")
    dealerLabel.config(text=f"Dealer Hand: {dealerText} (Value: {calculateHand(dealerHand)})")

'''

def updateCards():
    for widget in playerFrame.winfo_children():
        widget.destroy()
    for widget in dealerFrame.winfo_children():
        widget.destroy()

    for rank, suit in playerHand:
        img = Image.open(f"cards/{rank}_of_{suit}.png").resize((100,150))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(playerFrame, image=photo, bg="#006400")
        label.image = photo
        label.pack(side=tk.LEFT, padx=5)

    for i, (rank, suit) in enumerate(dealerHand):
        if i == 0 and not dealerRevealed:
            img = Image.open("cards/back.png").resize((100,150))
        else:
            img = Image.open(f"cards/{rank}_of_{suit}.png").resize((100,150))
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(dealerFrame, image=photo, bg="#006400")
        label.image = photo
        label.pack(side=tk.LEFT, padx=5)

    playerValueLabel.config(text=f"Player Value: {calculateHand(playerHand)}")

    if dealerRevealed:
        dealerValueLabel.config(text=f"Dealer Value: {calculateHand(dealerHand)}")
    else:
        dealerValueLabel.config(text="Dealer Value: ?")

def startGame():
    global playerHand, dealerHand, dealerRevealed
    dealerRevealed = False
    newDeck()
    playerHand = [deck.pop(), deck.pop()]
    dealerHand = [deck.pop(), deck.pop()]
    updateCards()
    statusLabel.config(text="Game has started: hit or stand?")
    hitButton.config(state="normal")
    standButton.config(state="normal")

def hit():
    dealCard(playerHand)
    updateCards()
    if calculateHand(playerHand) > 21:
        statusLabel.config(text="You busted, dealer wins")
        hitButton.config(state="disabled")
        standButton.config(state="disabled")
        revealDealer()

'''
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

'''
def stand():
    global reveal_dealer
    revealDealer()
    while calculateHand(dealerHand) < 17:
        dealCard(dealerHand)
        updateCards()
    playerScore = calculateHand(playerHand)
    dealerScore = calculateHand(dealerHand)

    if dealerScore > 21 or playerScore > dealerScore:
        statusLabel.config(text="You Win!")
    elif dealerScore == playerScore:
        statusLabel.config(text="You tied with the dealer")
    else:
        statusLabel.config(text="Dealer wins, you lost lol")

    hitButton.config(state="disabled")
    standButton.config(state="disabled")

def revealDealer():
    global dealerRevealed
    dealerRevealed = True
    updateCards()


root = tk.Tk()
root.title("Blackjack in Python")
root.config(bg="#006400")

statusLabel = tk.Label(root, text="Welcome to Blackjack", font=("Georgia", 20), bg="#006400", fg="white")
statusLabel.pack(pady=20)

playerFrame = tk.Frame(root, bg="#006400")
playerFrame.pack(pady=10)

dealerFrame = tk.Frame(root, bg="#006400")
dealerFrame.pack(pady=10)

playerValueLabel = tk.Label(root, text="Player Value: 0", font=("Georgia", 16), bg="#006400", fg="white")
playerValueLabel.pack(pady=5)

dealerValueLabel = tk.Label(root, text="Dealer Value: 0", font=("Georgia", 16), bg="#006400", fg="white")
dealerValueLabel.pack(pady=5)


buttonFrame = tk.Frame(root, bg="#006400")
buttonFrame.pack(pady=20)


hitButton = tk.Button(buttonFrame, text="Hit", font=("Georgia", 14), bg="white", command=hit, state="disabled")
hitButton.grid(row=0, column=10, padx=10)

standButton = tk.Button(buttonFrame, text="Stand", font=("Georgia", 14), bg="white", command=stand, state="disabled")
standButton.grid(row=0, column=1, padx=10)

startButton = tk.Button(buttonFrame, text="Start Game", font=("Georgia", 14), bg="yellow", command=startGame)
startButton.grid(row=0, column=2, padx=10)

deck = []
playerHand = []
dealerHand = []
dealerRevealed = False



root.mainloop()