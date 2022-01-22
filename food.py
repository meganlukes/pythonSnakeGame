from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()
      

    def refresh(self):
        new_x = random.randint(-280, 280)
        new_y = random.randint(-280, 260)
        self.goto(new_x, new_y)