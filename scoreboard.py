from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        with open("game_data.txt", mode="r") as file:
            high_score = file.read()
            super().__init__()
            self.score = 0
            self.high_score = int(high_score)
            self.color("white")
            self.penup()
            self.goto(0, 270)
            self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
            self.hideturtle()
            self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} HighScore: {self.high_score}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER: {self.score}", align=ALIGN, font=FONT)
    #

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("game_data.txt", mode="w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
