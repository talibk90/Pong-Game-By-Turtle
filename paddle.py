from turtle import Turtle
UP = 0
DOWN = 180

class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.y = 0
        self.x =x
        self.goto(self.x, self.y)

    def up(self):
        self.y += 50
        if self.y > 250:
            self.y = 250
        self.goto(self.x, self.y)



    def down(self):

        self.y -= 50
        if self.y < -250:
            self.y = -250
        self.goto(self.x, self.y)

    