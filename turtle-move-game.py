from turtle import Turtle,Screen

tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()

# SETTING DIRECTIONS
def moveForward():
    tim.forward(50)

def moveBackward():
    tim.backward(50)

def moveLeft():
    tim.left(90)

def moveRight():
    tim.right(90)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# SETTING KEYBOARD CONTROL
screen.listen()
screen.onkey(key="w", fun=moveForward)
screen.onkey(key="a", fun=moveLeft)
screen.onkey(key="s", fun=moveBackward)
screen.onkey(key="d", fun=moveRight)
screen.onkey(clear, "x")
screen.exitonclick()


# # HOW TO OPERATE :
# 1. Controls
#     W = forward
#     s = backward
#     a = turn right
#     d = turn left
# 2. run, and let's play games
# 3. click on screen if you want to end this game