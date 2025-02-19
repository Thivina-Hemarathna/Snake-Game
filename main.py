from turtle import Screen
import time

from layout import Layout
from scoreboard import ScoreBoard
from snake import Snake
from food import Food

screen=Screen()
screen.bgcolor("black")
screen.title("The Snake Game")
screen.setup(800,800)
screen.tracer(0)

lay=Layout()
snake=Snake()
food=Food()
scoreboard=ScoreBoard()

snake.createSnake()

screen.listen()

screen.onkeypress(key="Up", fun=snake.go_up)
screen.onkeypress(key="Down", fun=snake.go_down)
screen.onkeypress(key="Left", fun=snake.go_left)
screen.onkeypress(key="Right", fun=snake.go_right)
game_on=True
speed=0.15

while game_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-300:
        game_on=False
        scoreboard.game_over()

    for segment in snake.segments:

        if segment == snake.head:
            pass
        elif snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()

    if scoreboard.score>5 and scoreboard.score<10:
        speed=0.1
    elif scoreboard.score>10 and scoreboard.score<15:
        speed=0.08
    elif scoreboard.score > 15 and scoreboard.score < 20:
        speed = 0.05
    elif scoreboard.score > 20:
        speed = 0.03


screen.exitonclick()