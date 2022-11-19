# from re import S
# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)

# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fd(100)
# my_screen = Screen()
# my_screen.bgcolor('gray')

# print(my_screen.canvheight)
# my_screen.exitonclick()

from calendar import c
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pickachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align["Pokemon Name"] = "c"
table.align["Type"] = "c"

print(table)
