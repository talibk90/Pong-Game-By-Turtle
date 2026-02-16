from turtle import Turtle, Screen
from paddle import Paddle
from control import Control
from ball import Ball
import time
from scoreboard import Score
import winsound

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong - Game by TALIB")
left_paddle = Paddle(-350)
right_paddle = Paddle(350)
line = Control()
line.draw_center_line()
ball = Ball()


name1 = screen.textinput(title="Left Player", prompt="Enter Player 1 name: ")
name2 = screen.textinput(title="Right Player", prompt="Enter Player 2 name: ")

left_score = Score(name1, -200, 250)
right_score = Score(name2, 200, 250)

screen.listen()
# left player uses W/S, right player uses Up/Down
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


is_paused = False
def toggle_pause():
    global is_paused
    is_paused = not is_paused
screen.onkey(toggle_pause, "space")

def reset_game():
    global is_paused, is_Game_On
    is_paused = False
    is_Game_On = True
    ball.ball_reset()
    left_score.reset_score()
    right_score.reset_score()
    writer.clear()

screen.onkey(reset_game, "r")


writer = Turtle()
writer.hideturtle()
writer.color("white")




is_Game_On = True
while True:
    time.sleep(ball.ballspeed)
    try:
        screen.update()
        if is_paused or not is_Game_On:
            continue
        ball.move()
    except:
        break

    # if collide with walls then bounce (only when moving toward the wall)
    if ball.ycor() > 280  or ball.ycor() < -280:
        ball.bounce()

    if (ball.distance(right_paddle) < 50 and ball.xcor() >320 and ball.xmove> 0) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320 and ball.xmove< 0):
        winsound.PlaySound("topple.wav", winsound.SND_ASYNC)
        ball.bounce_x()


    # Right side player miss
    if(ball.xcor() >390):
        screen.tracer(0)
        ball.ball_reset()
        screen.update()
        left_score.update()
        time.sleep(0.5)


#  Left side play miss
    if(ball.xcor()< -390):
        screen.tracer(0)
        ball.ball_reset()
        screen.update()
        right_score.update()
        time.sleep(0.5)

    if(left_score.score ==10):
        is_Game_On = False
        writer.write(f"{name1} win", align="center", font=("Times New Roman", 30, "normal"))


    if(right_score.score ==10):
        is_Game_On = False
        writer.write(f"{name2} win", align="center", font=("Times New Roman", 30, "normal"))




screen.exitonclick()