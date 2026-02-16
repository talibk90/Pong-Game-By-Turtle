from turtle import Turtle
from random import random, randint, choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        # velocity per frame
        self.xmove = 10
        self.ymove = 10
        self.ballspeed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce(self):
        # vertical bounce (top/bottom walls)
        self.ymove *= -1

    def bounce_x(self):
        # horizontal bounce (paddles)
        self.xmove *= -1
        self.ballspeed *= 0.8

    def ball_reset(self):
        self.goto(0, 0)
        self.ballspeed = 0.1
        self.bounce_x()