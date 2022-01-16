from turtle import Screen, Turtle
import random, time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")
screen.title("Pink Python")
screen.tracer(0)

snake = []

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("DeepPink")
    new_segment.pu()
    new_segment.goto(position)
    snake.append(new_segment)



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








