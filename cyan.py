#name: Marcela Soriano Cornejo
#email: marcela.sorianocornejo40@myhunter.cuny.edu
#date: September 11, 2022
#This program draws out from the center to the top and right, increasing size and blue concentration with circular pen

import turtle
turtle.colormode(255)
t = turtle.Turtle()

for i in range(2):
    t.pendown()
    for j in range(0,255,10):
        t.pensize(j)
        t.color(0,j,j)
        t.forward(10)
    t.penup()
    t.backward(260)
    t.left(90)
t.right(90)