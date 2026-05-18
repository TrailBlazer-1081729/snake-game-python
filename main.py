from turtle import Turtle,Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")

screen.title("my_snake_game")
screen.tracer(0)
snake=Snake()
food=Food()
score=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


check=True
while check:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        food.restart()
        snake.extend()
        score.increase()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:

        score.game_over()
        check = False

    for position in snake.list:
        if not snake.head== position:
            if snake.head.distance(position)<10:
                check=False
                score.game_over()
        else:
            pass




screen.exitonclick()