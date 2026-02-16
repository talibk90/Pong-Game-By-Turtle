from turtle import Turtle


class Score(Turtle):

    def __init__(self, name, xpos, ypos):
        super().__init__()
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.goto(xpos, ypos)
        self.write(f"{self.name}'s Score: {self.score}", align="center", font=("Times New Roman", 18, "normal"))


    def update(self):
        self.score +=1
        self.clear()
        self.write(f"{self.name}'s Score: {self.score}", align="center", font=("Times New Roman", 18, "normal"))

    def reset_score(self):
        self.score = 0
        self.clear()
        self.write(f"{self.name}'s Score: {self.score}", align="center", font=("Times New Roman", 18, "normal"))



