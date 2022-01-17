from turtle import Screen, Turtle
import random, time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Pink Python")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food) < 15:
        print("yummy")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.snake:
        if segment == snake.snake[0]:
            pass
        elif snake.snake[0].distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()








