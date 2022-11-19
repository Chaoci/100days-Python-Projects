from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height =400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-100, -50, 0, 50, 100, 150 ]
all_turtle = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -225, y= random.randint(-200, 200))
    all_turtle.append(new_turtle)
    
if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        
    

# pen.speed('fastest')

# def move_forward():
#     pen.fd(10)

# def move_backward():
#     pen.backward(10)

# def turn_left():
#     new_heading = pen.heading() + 10
#     pen.setheading(new_heading)

# def turn_right():
#     new_heading = pen.heading() - 10
#     pen.setheading(new_heading)
    
# def clear():
#     pen.clear()
#     pen.penup()
#     pen.home()
#     pen.pendown()   

# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")

screen.exitonclick()

