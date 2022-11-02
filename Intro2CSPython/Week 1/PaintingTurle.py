import turtle
from turtle import *

def rectangle():
    turtle.color("cyan")
    turtle.begin_fill()  
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.end_fill()
    
    
def nestedCircle():
    turtle.color("Black", "Red")
    turtle.begin_fill()
    turtle.circle(20)
    turtle.circle(15) 
    turtle.forward(150)
    turtle.circle(20)
    turtle.circle(15) 
    turtle.end_fill()
    
def triangle(edge=10):
    turtle.color("Black")
    turtle.begin_fill()
    turtle.left(120)
    turtle.forward(edge)
    turtle.left(120)
    turtle.forward(edge) 
    turtle.left(120)
    turtle.forward(edge) 
    turtle.end_fill()
    

nestedCircle()
rectangle()
turtle.penup()
turtle.goto(110, -50)
turtle.pendown()
turtle.color("Black")
turtle.begin_fill()
turtle.circle(10)
turtle.penup()
turtle.goto(30, -50)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(80, -90)
turtle.pendown()
triangle(edge=20)
turtle.right(10)
turtle.penup()
turtle.goto(110, -100)
turtle.pendown()
turtle.down()
turtle.left(90)
turtle.circle(40, -160)
turtle.up()
