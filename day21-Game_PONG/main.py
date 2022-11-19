from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
r_score = (100, 200)
l_score = (-100,200)
screen = Screen()
screen.title('My PONG Game')
screen.bgcolor('black')
screen.setup(width = 800, height = 600)
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on =  True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    #上下的牆壁能夠回彈
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    
    # Detect collision with right paddle
    # paddle可以把球反彈回去
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        
    # Detect that lost the point
    # seperate the left side and right side because of needing to calculate the points
    if ball.xcor() > 380:
        ball.resset_position()
        score.left_player()
    
    if ball.xcor() < -380:
        ball.resset_position()
        score.right_player()

    if score.left_scores == 2:
        score.gameover(score.left_scores)
        game_is_on = False
    
    if score.right_scores == 2:
        score.gameover(score.right_scores)
        game_is_on = False






screen.exitonclick()