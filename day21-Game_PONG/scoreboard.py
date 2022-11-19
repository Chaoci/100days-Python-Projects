from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
POINT_FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.left_scores = 0
        self.right_scores = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(100, 200)
        self.write(self.right_scores, align="center", font = POINT_FONT)
        self.goto(-100, 200)
        self.write(self.left_scores, align="center", font = POINT_FONT)
        
    def left_player(self):
        self.left_scores += 1
        self.clear()
        self.update_scoreboard()
        
        
    def right_player(self):
        self.right_scores += 1
        self.clear()
        self.update_scoreboard()
        
        
    def gameover(self, final_score):
        self.goto(0, 0)
        self.write( f"Game Over", 
            move=False, 
            align='center', 
            font=FONT
        )
        if final_score == self.left_scores:
            self.goto(0, -20)
            self.write( f"Left Player Win!", 
            move=False, 
            align='center', 
            font=FONT
            )
        elif final_score == self.right_scores:
            self.goto(0, -20)
            self.write( f"Right Player Win!", 
            move=False, 
            align='center', 
            font=FONT
            )