from turtle import Turtle, Screen
import random

colors = ['pink', "DarkOrchid", "orange", "purple", "LightSeaGreen","wheat", "SlateGray"]

directions = [0, 90, 180, 270]
def random_color():
    r = random.randrange(1.0, 255)
    g = random.randrange(1.0, 255)
    b = random.randrange(1.0, 255)
    rgb = (r, g, b)
    return rgb

tim = Turtle()

tim.shape('circle')
tim.speed("fastest")

screen = Screen()
screen.colormode(255)
screen.bgcolor('gray')
screen.setup (width=800, height=500, startx=0, starty=0)
step = random.randrange(0,200)
for _ in range(step):
    tim.color(random_color())
    tim.pensize(10)
    tim.fd(30)
    tim.setheading(random.choice(directions))




screen.exitonclick()