import tkinter as tk

def startGame():
    print("Game has started, good luck!")

root = tk.Tk()
root.title("This is Blackjack in Python")
root.geometry("600x400")

welcomeLabel = tk.Label(root, text="Welcome to Blackjack", font=("Arial", 20))
welcomeLabel.pack(pady=20)

startButton = tk.Button(root, text="Start Game", font=("Arial", 14), command=startGame)
startButton.pack(pady=10)

root.mainloop()