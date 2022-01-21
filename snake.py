from turtle import Screen, Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance= 20

class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("DeepPink")
        new_segment.pu()
        new_segment.goto(position)
        self.snake.append(new_segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg-1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(move_distance)

    def reset(self):
        self.snake.clear()
        self.create_snake()

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)
    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)
    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)