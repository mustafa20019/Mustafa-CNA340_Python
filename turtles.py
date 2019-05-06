import turtle
import random

wn = turtle.Screen()  # create a screen
wn.bgcolor('lightblue')
wn.title("Turtle Race")

lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

andy.up()
lance.up()
andy.goto(-100, 20)
lance.goto(-100, -20)

start = turtle.Turtle()  # OPTIONAL-
start.hideturtle()

andyTotalDistance = 0
lanceTotalDistance = 0

for i in range(150):

    andyDistance = random.randrange(1, 5)
    lanceDistance = random.randrange(1, 5)
    andy.forward(andyDistance)
    lance.forward(lanceDistance)

    andyTotalDistance = andyTotalDistance + andyDistance
    lanceTotalDistance = lanceTotalDistance + lanceDistance


for eachInt in range(145):
    if andyTotalDistance > lanceTotalDistance:
        start.write("Andy is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    elif lanceTotalDistance > andyTotalDistance:
        start.write("Lance is the winner!", move=False, align="center", font=("Arial", 25, "normal"))
    else: print("Tie Game")

wn.exitonclick()
