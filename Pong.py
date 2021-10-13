#Import the turtle library
import turtle

#The Main Game Window 
window = turtle.Screen()
window.title("GK's Ping Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer()

#Left Paddle
leftPaddle = turtle.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("red")
leftPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
leftPaddle.penup()
leftPaddle.goto(-350, 0)

#Right Paddle
rightPaddle = turtle.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("blue")
rightPaddle.shapesize(stretch_wid = 5, stretch_len = 1)
rightPaddle.penup()
rightPaddle.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("purple")
ball.penup()
ball.goto(0,0)
ball.dx = 8
ball.dy = -5

#Movement Functions
def leftPaddleUp():
    y = leftPaddle.ycor()
    y += 20
    leftPaddle.sety(y)

def leftPaddleDown():
    y = leftPaddle.ycor()
    y -= 20
    leftPaddle.sety(y)

def rightPaddleUp():
    y = rightPaddle.ycor()
    y += 20
    rightPaddle.sety(y)

def rightPaddleDown():
    y = rightPaddle.ycor()
    y -= 20
    rightPaddle.sety(y)    

#Controls
window.listen()
window.onkeypress(leftPaddleUp, "w")
window.onkeypress(leftPaddleDown, "s")
window.onkeypress(rightPaddleUp, "Up")
window.onkeypress(rightPaddleDown, "Down")

#This while loop keeps the game running
while True:
    window.update()

#The code for the ball is within the while loop as the ball only moves while the game is active
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

#Collisions with the window
    if ball.ycor() > 285:
        ball.sety(285)
        ball.dy *= -1   #Reverses the direction

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1   #Reverses the direction

    if ball.xcor() > 425:
        ball.goto(0, 0)
        ball.dx *= -1   #If the ball is scored on the enemy side, it is sent to the opponent's side, from the center

    if ball.xcor() < -425:
        ball.goto(0, 0)
        ball.dx *= -1  

#Collisions with the paddle
    if (ball.xcor() > 325 and ball.xcor() < 340) and (ball.ycor() < rightPaddle.ycor() + 50 and ball.ycor() > rightPaddle.ycor() - 50):
        ball.setx(325)
        ball.dx *= -1

    if (ball.xcor() < -325 and ball.xcor() > -340) and (ball.ycor() < leftPaddle.ycor() + 50 and ball.ycor() > leftPaddle.ycor() - 50):
        ball.setx(-325)
        ball.dx *= -1