from turtle import Screen, Turtle
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Pink Python")
snake = []

for turtles in range(3):
    new_turtle = Turtle("square")
    new_turtle.color("DeepPink")
    new_turtle.goto((-20 * turtles), 0)
    snake.append(new_turtle)
















screen.exitonclick()