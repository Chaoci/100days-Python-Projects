from turtle import Turtle, Screen
import random
def random_color():
    r = random.randrange(1.0, 255)
    g = random.randrange(1.0, 255)
    b = random.randrange(1.0, 255)
    rgb = (r, g, b)
    return rgb
pen = Turtle()
pen.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.bgcolor("lightgray")
screen.setup (width=800, height=500, startx=0, starty=0)


# for _ in range(100):
#     pen.color(random_color())
#     pen.circle(100)
#     pen.right(3.6)


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        pen.color(random_color())
        pen.circle(100)
        pen.setheading(pen.heading() + size_of_gap)
        
draw_spirograph(3.6)
screen.exitonclick()

    