from turtle import Screen, Turtle
import random, time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Pink Python")
screen.tracer(0)

snake = []

for turtles in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("DeepPink")
    new_turtle.pu()
    new_turtle.goto((-20 * turtles), 0)
    snake.append(new_turtle)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in range(len(snake) - 1, 0, -1):
        new_x = snake[seg - 1].xcor()
        new_y = snake[seg-1].ycor()
        snake[seg].goto(new_x, new_y)
    snake[0].forward(20)




screen.exitonclick()








