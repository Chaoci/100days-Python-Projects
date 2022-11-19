from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
located = Turtle()
located.hideturtle()
data_states = pd.read_csv("day25-OpenData/us-states-game-start/50_states.csv")

states_name = data_states.state.to_list()
states_x = data_states.x.to_list()
states_y = data_states.y.to_list()
FONT = ("Courier", 12, "normal")


print(states_name[1])
print(states_x[1])
print(states_y[1])


screen.bgpic("day25-OpenData/us-states-game-start/blank_states_img.gif")
screen.setup(width=750, height= 500)

game_is_on = True
score = 0
while game_is_on:
    ask = screen.textinput(title=f"{score}/50 states correct", prompt="enter the name of states:")
    for i, name in enumerate(states_name):
        if ask == name:
            located.penup()
            located.goto(states_x[i], states_y[i])
            located.color('black')
            located.write(f"{name}", move=False, font=FONT)
            score +=1
            
        

screen.exitonclick()