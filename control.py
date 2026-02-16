from turtle import Turtle
class Control:


    def draw_center_line(self):
        self.line = Turtle()
        self.line.speed("fastest")
        self.line.color("white")
        self.line.penup()
        self.line.goto(0, -300)   # start from bottom
        self.line.setheading(90)  # face upward

        while self.line.ycor() < 300:
            self.line.pendown()
            self.line.forward(10)   # draw small line
            self.line.penup()
            self.line.forward(10)  # gap

        self.line.hideturtle()

