#Yout First Game you will look back on this a say you are trash lol
#Be Creative you brain is full of weird stuff

import turtle

# Display
nw = turtle.Screen()
nw.title("Can You Survive")
nw.bgcolor("Black")
nw.setup(width=800,height=800)
nw.tracer(0)


#PLayer Character
Player = turtle.Turtle()
Player.speed(0)
Player.shape("square")
Player.color("Blue")
Player.penup()
Player.goto(0,0)

# Functions
def Player_Right():
    x = Player.xcor()
    x += 20
    Player.setx(x)

def Player_Left():
    x = Player.xcor()
    x -= 20
    Player.setx(x)

def Player_Up():
    y = Player.ycor()
    y += 20
    Player.sety(y)

def Player_Down():
    y = Player.ycor()
    y -= 20
    Player.sety(y)

#Player Inputs
nw.listen()
nw.onkeypress(Player_Right, "d")

nw.listen()
nw.onkeypress(Player_Left, "a")

nw.listen()
nw.onkeypress(Player_Up, "w")

nw.listen()
nw.onkeypress(Player_Down, "s")












#Main Game Loop
while True:
    nw.update()