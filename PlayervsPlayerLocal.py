import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

deck = []
player1Hand = []
player2Hand = []
currentPlayer = 1

def newDeck():
    global deck
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)

def dealCard(hand):
    if deck:
        hand.append(deck.pop())

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

def updateCards():
    for frame in (p1Frame, p2Frame):
        for widget in frame.winfo_children():
            widget.destroy()
    
    for rank, suit in player1Hand:
        img = Image.open(f"cards/{rank}_of_{suit}.png").resize((100,150))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(p1Frame, image=photo, bg="#006400")
        lbl.image = photo
        lbl.pack(side=tk.LEFT, padx=5)

    for rank, suit in player2Hand:
        img = Image.open(f"cards/{rank}_of_{suit}.png").resize((100,150))
        photo = ImageTk.PhotoImage(img)
        lbl = tk.Label(p2Frame, image=photo, bg="#006400")
        lbl.image = photo
        lbl.pack(side=tk.LEFT, padx=5)

    p1ValueLabel.config(text=f"Player 1 Value: {calculateHand(player1Hand)}")
    p2ValueLabel.config(text=f"Player 2 Value: {calculateHand(player2Hand)}")

def startGame():
    global player1Hand, player2Hand, currentPlayer
    newDeck()
    player1Hand = [deck.pop(), deck.pop()]
    player2Hand = [deck.pop(), deck.pop()]
    currentPlayer = 1

    statusLabel.config(text="Player 1's Turn")
    hitButton.config(state="normal")
    standButton.config(state="normal")
    startButton.config(state="disabled")
    updateCards()

def hit():
    global currentPlayer
    if currentPlayer == 1:
        player1Hand.append(deck.pop())
        updateCards()
        if calculateHand(player1Hand) > 21:
            messagebox.showinfo("Bust!"," Player 1 has busted. Now it is Player 2's turn")
            switchTurn()
    else:
        player2Hand.append(deck.pop())
        updateCards()
        if calculateHand(player2Hand) > 21:
            messagebox.showinfo("Bust!", "Player 2 has busted.")
            endGame()


def stand():
    global currentPlayer
    if currentPlayer == 1:
        messagebox.showinfo("Stand", "Player 1 stands. Now it's Player 2's turn.")
        switchTurn()
    else:
        messagebox.showinfo("Stand", "Player 2 stands.")
        endGame()

def switchTurn():
    global currentPlayer
    if currentPlayer == 1:
        currentPlayer = 2
        statusLabel.config(text="Player 2's Turn")
        messagebox.showinfo("Turn", "Player 2's turn.")
    else:
        endGame()

def endGame():
    player1Val = calculateHand(player1Hand)
    player2Val = calculateHand(player2Hand)

    result = ""
    if player1Val > 21 and player2Val > 21:
        result = "Both players busted lol"
    elif player1Val > 21:
        result = "Player 2 wins!"
    elif player2Val > 21:
        result = "Player 1 wins!"
    elif player1Val > player2Val:
        result = "Player 1 wins!"
    elif player2Val > player1Val:
        result = "Player 2 wins!"
    else:
        result = "Both players have tied."

    messagebox.showinfo("Game Over", result)
    statusLabel.config(text=result)
    hitButton.config(state="disabled")
    standButton.config(state="disabled")
    startButton.config(state="normal")



root = tk.Tk()
root.title("Two Player Blackjack in Python")
root.config(bg="#006400")

statusLabel = tk.Label(root, text="Welcome to Blackjack", font=("Georgia", 20), bg="#006400", fg="white")
statusLabel.pack(pady=20)


p1Label = tk.Label(root, text="Player 1", font=("Georgia", 16), bg="#006400", fg="white")
p1Label.pack()
p1Frame = tk.Frame(root, bg="#006400")
p1Frame.pack(pady=10)
p1ValueLabel = tk.Label(root, text="Player 1 Value: 0", font=("Georgia", 14), bg="#006400", fg="white")
p1ValueLabel.pack(pady=5)

p2Label = tk.Label(root, text="Player 2", font=("Georgia", 16), bg="#006400", fg="white")
p2Label.pack()
p2Frame = tk.Frame(root, bg="#006400")
p2Frame.pack(pady=10)
p2ValueLabel = tk.Label(root, text="Player 2 Value: 0", font=("Georgia", 14), bg="#006400", fg="white")
p2ValueLabel.pack(pady=5)




buttonFrame = tk.Frame(root, bg="#006400")
buttonFrame.pack(pady=20)

hitButton = tk.Button(buttonFrame, text="Hit", font=("Georgia", 14), bg="white", command=hit, state="disabled")
hitButton.grid(row=0, column=10, padx=10)

standButton = tk.Button(buttonFrame, text="Stand", font=("Georgia", 14), bg="white", command=stand, state="disabled")
standButton.grid(row=0, column=1, padx=10)

startButton = tk.Button(buttonFrame, text="Start Game", font=("Georgia", 14), bg="yellow", command=startGame)
startButton.grid(row=0, column=2, padx=10)



root.mainloop()