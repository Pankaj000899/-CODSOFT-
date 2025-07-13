from tkinter import *
import random

player_point = 0
computer_point = 0

def reset():
    global player_point
    global computer_point
    player_point = 0
    computer_point = 0

    player_label.config(text="Player \u27A4",font = "Bierstadt 15")
    computer_label.config(text="Computer \u27A4",font = "Bierstadt 15")
    result_label.config(text="Result",font = "Bierstadt 15 bold")
    score_label.config(text = "Player  -  0 \U0001F525 Computer - 0",font = "Bierstadt 15")

def score(player, computer):
    global player_point
    global computer_point
    if (
        (player == "\U0001F5FF" and computer == "\u270C") or
        (player == "\U0001F4C4" and computer == "\U0001F5FF") or
        (player == "\u270C" and computer == "\U0001F4C4")
    ):
        player_point += 1
        return "Player win"

    elif (
        (computer == "\U0001F5FF" and player == "\u270C") or
        (computer == "\U0001F4C4" and player == "\U0001F5FF") or
        (computer == "\u270C" and player == "\U0001F4C4")
    ):
        computer_point += 1
        return "Computer win"

    elif (computer == player):
        return "Match draw"

def start(player):
    computer = random.choice(["\U0001F5FF", "\U0001F4C4", "\u270C"])
    Score = score(player, computer)

    player_label.config(text=f"You Chose \u27A4 {player}")
    computer_label.config(text=f"Computer Chose \u27A4 {computer}")
    result_label.config(text=f"Result \u27A4 {Score}")
    score_label.config(text=f"Player  - {player_point} \U0001F525 Computer - {computer_point}")

root = Tk()

root.title("Rock Paper Scissors Game")
root.geometry("400x400")

root.resizable(False, False)
Label(root,text = "Rock Paper Scissors",font = "Bierstadt 20 bold").pack()
Label(root,text = "Select any of them",font = "Bierstadt 15").pack()

frame = Frame(root)
frame.pack()

rock_button = Button(frame,text="\U0001F5FF",font = "Bierstadt 15",width = 5,height = 2,bg = "white",command = lambda: start("\U0001F5FF"))
rock_button.grid(row = 0, column = 0)

paper_button = Button(frame,text="\U0001F4C4",font = "Bierstadt 15",width = 5,height = 2,bg = "black",fg = "white",command = lambda: start("\U0001F4C4"))
paper_button.grid(row = 0, column = 1)

scissors_button = Button(frame,text="\u270C",font = "Bierstadt 15",width = 5,height = 2,bg = "white",fg = "red",command = lambda: start("\u270C"))
scissors_button.grid(row = 0, column = 2)

player_label = Label(root,text = "Player \u27A4",font = "Bierstadt 15")
player_label.pack()

computer_label = Label(root,text = "Computer \u27A4",font = "Bierstadt 15")
computer_label.pack()

result_label = Label(root,text = "Result",font = "Bierstadt 15 bold")
result_label.pack()

score_label = Label(root,text = "Player  -  0 \U0001F525 Computer - 0",font = "Bierstadt 15")
score_label.pack()

reset_button = Button(root,text = "Play again",font = "Bierstadt 15",width = 10,height = 2,fg = "blue",bg = "pink",command = reset)
reset_button.pack()

root.mainloop()
