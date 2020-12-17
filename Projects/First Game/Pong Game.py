#Pong Game

import turtle   

nw = turtle.Screen()
nw.title("Pong by Chandler King")
nw.bgcolor("black")     
nw.setup(width=800,height=600)
nw.tracer(0)

# Score
score_a = 0
score_b = 0


# Paddle 1
paddel_1 = turtle.Turtle()
paddel_1.speed(0)
paddel_1.shape("square")
paddel_1.color("Blue")
paddel_1.shapesize(stretch_wid=5, stretch_len=1)
paddel_1.penup()
paddel_1.goto(-350, 0)

# Paddle 2
paddel_2 = turtle.Turtle()
paddel_2.speed(0)
paddel_2.shape("square")
paddel_2.color("Red")
paddel_2.shapesize(stretch_wid=5, stretch_len=1)
paddel_2.penup()
paddel_2.goto(350, 0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("Yellow")
Ball.penup()
Ball.goto(0, 0)
Ball.dx = .18
Ball.dy = .18

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Payer A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddel_1_up():
    y = paddel_1.ycor()
    y += 20
    paddel_1.sety(y)

def paddel_1_down():
    y = paddel_1.ycor()
    y -= 20
    paddel_1.sety(y)

def paddel_2_up():
    y = paddel_2.ycor()
    y += 20
    paddel_2.sety(y)

def paddel_2_down():
    y = paddel_2.ycor()
    y -= 20
    paddel_2.sety(y)

# keyboard binding
nw.listen()
nw.onkeypress(paddel_1_up, "w")

nw.listen()
nw.onkeypress(paddel_1_down, "s")

nw.listen()
nw.onkeypress(paddel_2_up, "Up")

nw.listen()
nw.onkeypress(paddel_2_down, "Down")





#main game loop
while True:
    nw.update()

    #Moving the Ball
    Ball.setx(Ball.xcor() + Ball.dx)
    Ball.sety(Ball.ycor() + Ball.dy)

    #Boarder Checking
    if Ball.ycor() > 290:
        Ball.sety(290)
        Ball.dy *= -1

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *= -1
    
    if  Ball.xcor() > 390:
        Ball.goto(0, 0 )
        Ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Payer A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    if  Ball.xcor() < -390:
        Ball.goto(0, 0 )
        Ball.dx *= -1
        score_b *= 1
        pen.clear()
        pen.write("Payer A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # Paddle and ball collisions
    if (Ball.xcor() > 340 and Ball.xcor() < 350) and (Ball.ycor() < paddel_2.ycor() + 40 and Ball.ycor() > paddel_2.ycor() -40):
        Ball.setx(340)
        Ball.dx *= -1

    if (Ball.xcor() < -340 and Ball.xcor() > -350) and (Ball.ycor() < paddel_1.ycor() + 40 and Ball.ycor() > paddel_1.ycor() -40):
        Ball.setx(-340)
        Ball.dx *= -1




