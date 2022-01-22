from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_scores.txt", mode="r") as file:
            high_score = file.read()
        self.write(f"Score: {self.score}  High Score: {high_score}", align="center", font=("Arial", 24, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_scores.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()