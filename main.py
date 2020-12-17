import pandas as pd
import turtle
from turtle import Turtle

# Setting up the screen
screen = turtle.Screen()
screen.title("U.S.A STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Setting up the turtle that will display the state name once guessed correctly
writer = Turtle()
writer.penup()
writer.hideturtle()

# Reading the data
data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()

# Tracks the number of correct guesses
correct = 0
guessed_states = []
# Loop runs until the user guesses all 50 cases
while correct <50:

    # Prompt
    guess = screen.textinput(title= f"{correct}/50", prompt="Name a state: ").title()

    # Checks if the guess is an actual state and then displays it on the map
    if guess in all_states:
        guessed_states.append(guess)
        x = int(data[data["state"] == guess]["x"])
        y = int(data[data["state"] == guess]["y"])
        writer.goto(x, y)
        writer.write(guess)
        correct += 1

    # Breaks the while loop
    if guess == "Exit":
        break

# Checks to see what states were missed
states_missed = []
for state in all_states:
    if state not in guessed_states:
        states_missed.append(state)

# Coverts the missed states into a data frame which is then written on to a csv file
df = pd.DataFrame(states_missed,columns=["States"])
df.to_csv("Missed_States")
