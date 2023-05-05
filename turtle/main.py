import turtle
from turtle import Turtle,Screen
import random
tur = Turtle()
tur.shape("circle")
turtle.colormode(255)
# tur.color("blue")
# tur.forward(50)
# tur.forward(100)
# tur.right(90)
# tur.forward(100)
# tur.right(90)
# tur.forward(100)
# tur.right(90)
# tur.forward(100)
# myscreen = Screen()
# myscreen.exitonclick()
# for l in range(15):
#     tur.forward(10)
#     tur.penup()
#     tur.forward(10)
#     tur.pendown()
#
# myscreen = Screen()
# myscreen.exitonclick()

"""
f = 3

colors = ["IndianRed","wheat","SlateGray","SeaGreen"]
while f != 10:
    tur.color(random.choice(colors))
    for i in range(f):

        tur.forward(100)
        tur.left(180-(f-2)*180/f)

    f += 1

myscreen = Screen()
myscreen.exitonclick()

"""
# print(myscreen.canvwidth, myscreen.canvheight)

# from prettytable import PrettyTable
# table = PrettyTable()
# table.add_column("city name",["a","b","c"])
# table.add_column("type",["x","y","z"])
# table.add_row(['d','r'])
# table.align = "l"
# print(table)
'''
tur.pensize(5)
tur.speed(50)
colors = ["IndianRed","wheat","SlateGray","SeaGreen"]
moving = True
s = 0
while s != 500:
    # tur.color(random.choice(colors))
    tur.setheading(90*random.randint(0,3))
    tur.forward(10)
    tur.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    # tur.left(90*random.randint(0,2))
    s+=1


'''

'''spirograph

tur.speed(500)
angle = 0
while angle != 360:
    tur.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tur.circle(100)
    tur.left(10)
    angle+=10 '''





myscreen = Screen()
myscreen.exitonclick()