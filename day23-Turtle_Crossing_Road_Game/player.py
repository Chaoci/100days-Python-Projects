from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.shapesize(stretch_wid= 1,stretch_len=1)
        self.color('lightgreen')
        self.goto(STARTING_POSITION)

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)
        
    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
        
    def move_left(self):
        new_x = self.xcor() - 25
        self.goto(new_x, self.ycor())
        
    def move_right(self):
        new_x = self.xcor() + 25
        self.goto(new_x, self.ycor())
    
    def stop(self):
        self.goto(self.xcor(), self.ycor())
        
    def resset_position(self):
        self.goto(STARTING_POSITION)