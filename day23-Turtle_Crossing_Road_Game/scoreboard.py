from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(-280, 270)
        self.level = 1
        self.write(f"level: {self.level}", move=False,font= FONT)
        
    def score_update(self):
        self.clear()
        self.goto(-280, 270)
        self.write(f"level: {self.level}", move=False,font= FONT)
    
    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", 
            move=False, 
            align='center', 
            font=FONT
        )
