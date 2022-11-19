import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

speed = 0.1
screen = Screen()
screen.bgcolor('gray')
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car = CarManager()


screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left,"Left")
screen.onkey(player.move_right,"Right")
# try to build the wall
    
if player.xcor() > 290:
    screen.onkey(player.stop, "Right")

if player.xcor() < 290:
    screen.onkey(player.move_right,"Right")
    

if player.xcor() < -290:
    screen.onkey(player.stop, "Left")
    
if player.xcor() > -290:
    screen.onkey(player.move_left, "Left")

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    car.create_cars()
    car.move_cars()
    
    if player.ycor() > 290:
        scoreboard.level += 1
        player.resset_position()
        scoreboard.score_update()
        speed  *= 0.9

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.gameover()
            
screen.exitonclick()