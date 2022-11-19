# import colorgram

# colors = colorgram.extract('day18-code\hirst-painting\image.jpg', 10)
# extract_colors = []
# for i, image_color in enumerate(colors):
#     extract_colors.append(colors[i].rgb[0:])

# print(extract_colors)
from turtle import Turtle, Screen
import random

pen = Turtle()

screen = Screen()
screen.setup (width=800, height=500, startx=0, starty=0)
screen.colormode(255)
color_list = [(236, 236, 242), (240, 229, 236), (241, 231, 220), (224, 162, 69), (228, 240, 235), (19, 44, 82), (133, 62, 85), (171, 65, 45), (125, 39, 60), (23, 85, 61)]

pen.speed('fastest')
pen.penup()
pen.setheading(225)
pen.fd(300)
pen.setheading(0)
num = 100

def fd_dot():
    for dot_count in range(1, num+1):
        pen.penup()
        pen.fd(50)
        pen.dot(20, random.choice(color_list))
        
        if dot_count % 10 == 0:
            pen.setheading(90)
            pen.fd(50)
            pen.setheading(180)
            pen.fd(500)
            pen.setheading(0)
    pen.ht()
fd_dot()




screen.exitonclick()