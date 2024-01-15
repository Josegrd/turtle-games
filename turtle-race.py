from turtle import Turtle, Screen
import random

# set screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")

# set turtle
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []
y_axis = -80

for tur in colors:
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(x=-230, y=y_axis)
    t.color(tur)
    y_axis += 30
    all_turtle.append(t)


# set game option
game_start = False

if user_bet:
    game_start = True

while game_start:
    for tim in all_turtle:
        if tim.xcor() > 230:
            game_start = False
            color_won = tim.pencolor()
            if color_won == user_bet:
                print(f"You Won!, the {color_won} turtle is won")
            else:
                print(f"You Lose, the {color_won} turtle is won")
        random_distance = random.randint(0, 10)
        tim.forward(random_distance)

screen.exitonclick()


# HOW TO OPERATE
# 1. input your gacok
# 2. turtle akan otomatis balapan
# 3. untuk keluar klik layar