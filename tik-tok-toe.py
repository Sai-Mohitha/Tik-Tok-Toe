from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("560x370")
root.title("Tic Tac Toe By mohitha")

# Set the background color
root.configure(bg="lightgray")

# Create a style for the buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 16), padding=5, width=5)

buttons = {}  # Dictionary to store button objects
player = 1

def checkwinner():
    for combo in [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]:
        if all(buttons[i]["text"] == "X" for i in combo):
            messagebox.showinfo("Winner", "Congratulations, Player 1 Is The Winner")
            return
        if all(buttons[i]["text"] == "O" for i in combo):
            messagebox.showinfo("Winner", "Congratulations, Player 2 Is The Winner")
            return

def buttonpressed(buttonNumber):
    global player
    if buttons[buttonNumber]["text"] == " ":
        if player == 1:
            buttons[buttonNumber].config(text="X")
            player = 2
        else:
            buttons[buttonNumber].config(text="O")
            player = 1
        checkwinner()
    else:
        messagebox.showinfo("Invalid Move", "This button has already been pressed. Please choose an empty one.")

# Create and place buttons
for i in range(1, 10):
    buttons[i] = ttk.Button(root, text=" ", command=lambda i=i: buttonpressed(i))
    buttons[i].grid(row=(i - 1) // 3, column=(i - 1) % 3, ipadx=50, ipady=50)

root.mainloop()
