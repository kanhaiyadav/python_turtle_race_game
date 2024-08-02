from turtle import Turtle, Screen
from random import randint

players = []
player = int(input("Enter no. of players: "))
colors = []
height_of_screen = 200 + (player - 1) * 50
for i in range(player):
    new_player = {
        "name": input(f"Player {i + 1}: "),
        "color": input("color: ")
    }
    colors.append(new_player["color"])
    players.append(new_player)

my_screen = Screen()
my_screen.setup(width=1000, height=height_of_screen)
timmy = Turtle()
timmy.penup()
timmy.goto(470, height_of_screen/2)
timmy.pendown()
timmy.pencolor("red")
timmy.goto(470, -(height_of_screen/2))

my_screen.textinput(title="Welcome to Turtle Race!!!", prompt="Enter play to star the game")

turtles = []
y_cor = -(height_of_screen / 2 - 100)
for i in range(player):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(2)
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-480, y_cor)
    turtles.append(new_turtle)
    y_cor += 50

w_color = ""
race = True
while race:
    for turtle in turtles:
        turtle.forward(randint(5, 10))
        if turtle.xcor() >= 460:
            w_color = turtle.pencolor()
            race = False
for player in players:
    if player["color"] == w_color:
        winner = player["name"]
        print(f"Congratulations {winner}, you won.")
my_screen.exitonclick()
