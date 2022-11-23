from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard  import ScoreBoard

import random,time
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
food=Food()
snake=Snake()

score=ScoreBoard()
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
game_on=True
screen.update()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <15:
        food.refresh()
        score.update_score()
        snake.extend()
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_on=False
        score.game_over()
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) <10 :
            game_on = False
            score.game_over()

















screen.exitonclick()