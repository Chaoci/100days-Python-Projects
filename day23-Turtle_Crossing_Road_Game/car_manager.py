from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        
    
    def create_cars(self):
        # it will create too many cars that turtle couldn't even move a step
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            new_car.setheading(180)    
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for cars in self.all_cars:
            cars.fd(STARTING_MOVE_DISTANCE)