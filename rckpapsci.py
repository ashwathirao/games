import random
from tkinter import *
import pyttsx3

engine=pyttsx3.init()
stats=[]
def get_winner(call):
    if random.random()<=(1/3):
        throw="rock"
    elif (1/3)<random.random()<=(2/3):
        throw="scissors"
    else:
        throw="paper"
    if (throw=="rock" and call=="paper") or (throw=="paper" and call=="scissors") or (throw=="scissors" and call=="rock"):
        sats.append("W")
        result="You Won !"
        engine.say("wow, You won this turn")
    elif throw==call:
        stats.append("D")
        engine.say("It's a draw")
        result="It's a Draw"
    else:
        stats.append("L")
        engine.say("Sorry, you lost this turn")
        result="You lost!"
    global output
    output.config(text="Computer's throw "+throw+" \n"+result)
def pass_scissors():
    get_winner("scissors")
def pass_paper():
    get_winner("paper")
def pass_rock():
    get_winner("rock")
root=tkinter.Tk()
scissors=tkinter.Button(root,text="Scissors",padx=10,pady=5,width=20,bg="violet",command=pass_scissors)
rock=tkinter.Button(root,text="Rock",padx=10,pady=5,width=20,bg="grey",command=pass_rock)
paper=tkinter.Button(root,text="Scissors",padx=10,pady=5,width=20,bg="pink",command=pass_paper)
output=tkinter.Label(root,width=20,fg="green",text="What is your call")
scissors.pack(side="left")
rock.pack(side="left")
paper.paper(side="left")
output.pack(side="right")
root.mainloop()
for i in stats:
    print(i,end=" ")
if stats.count("L")>stats.count("W"):
    print("Sorry you lost the game")
    engine.say("Sorry you lost the game")
elif stats.count("L")==stats.count("W"):
    print("Its a draw")
    engine.say("the game ended in draw")
else:
    print("You won the game")
    engine.say("You won the game")
engine.runAndWait()