from tkinter import *
import random
c_input=['Rock','Paper','Scissor']

#To making buttons active again for playing once the user clicks on play again button
def play_again():
    Rock_button["state"]="active"
    Rock_button.config(bg="red")
    Paper_button["state"]="active"
    Paper_button.config(bg="blue")
    Scissor_button["state"]="active"
    Scissor_button.config(bg="green")
    text1.config(text="Player")
    text2.config(text="VS")
    text3.config(text="Computer")
    text4.config(text="")

#For disabling buttons after the user selects input
def button_disable():
    Rock_button["state"] = "disable"
    Paper_button["state"] = "disable"
    Scissor_button["state"] = "disable"

#When the inout of user is ROCK
def rock():
    computer=random.choice(c_input)
    if computer=='Rock':
        result='DRAW'
    elif computer=='Paper':
        result='Computer Win'
    elif computer=='Scissor':
        result='Player Win'
    text1.config(text="Rock")
    text3.config(text=computer)
    text4.config(text=result)
    button_disable()

#When the inout of user is PAPER
def paper():
    computer=random.choice(c_input)
    if computer=='Rock':
        result='Player Win'
    elif computer=='Paper':
        result='DRAW'
    elif computer=='Scissor':
        result='Computer Win'
    text1.config(text="Paper")
    text3.config(text=computer)
    text4.config(text=result)
    button_disable()

#When the inout of user is SCISSOR
def scissor():
    computer=random.choice(c_input)
    if computer=='Rock':
        result='Computer Win'
    elif computer=='Paper':
        result='Player Win'
    elif computer=='Scissor':
        result='DRAW'
    text1.config(text="Scissor")
    text3.config(text=computer)
    text4.config(text=result)
    button_disable()

a=Tk()# Assigning a variable to tkinter module

#setting window dimension
a.geometry("500x500") 

#title of the window
a.title("Rock Paper Scissor Game")

# Adding label for the game
Label(a,text="Rock Paper Scissor",
      font="normal 20 bold",
      fg="purple",bg="cyan").pack(pady=20)

# Making a frame for text box 
frame = Frame(a)
frame.pack()
text1=Label(frame,text="Player",font=15)
text2=Label(frame,text="VS",font="normal 18 bold")
text3=Label(frame,text="Computer",font=15)

# For deploying text box
text1.pack(side=LEFT)
text2.pack(side=LEFT)
text3.pack(side=RIGHT)
text4=Label(a,text="",bg="cyan",font=12,width=20)
text4.pack(pady=60)

# Adding another frame for buttons
frame1=Frame(a)
frame1.pack()

#setting up buttons for assigning user's choice
Rock_button=Button(frame1, text="Rock",
            font=10, width=7,
            command=rock,bg="red")
Rock_button.pack(side=LEFT,padx=10,pady=10) # For the deployement of buttons

Paper_button=Button(frame1, text="Paper",
            font=10, width=7,
            command=paper,bg="blue")
Paper_button.pack(side=LEFT,padx=10,pady=10) # For the deployement of buttons

Scissor_button=Button(frame1, text="Scissor",
            font=10, width=7,
            command=scissor,bg="green")
Scissor_button.pack(side=LEFT,padx=10,pady=10) # For the deployement of buttons

#button to play again
Button(a,text="Play Again!!",
       font="bold 10",bg="pink",width=30,
       command=play_again).pack(padx=10,pady=10)

a.mainloop() #To execute tkinter GUI