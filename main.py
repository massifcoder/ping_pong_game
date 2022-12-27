"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle
import time

b1 =  turtle.Turtle()
b1.shape('square')
b2 =  turtle.Turtle()
b2.shape('square')
b3 =  turtle.Turtle()
b3.shape('square')
b1.penup()
b2.penup()
b3.penup()
b1.goto(-100,-200)
b1.color('white')
b2.goto(-80,-200)
b2.color('white')
b3.goto(-120,-200)
b3.color('white')
t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(500,400)
screen.bgcolor('yellow')
t.shape('circle')
t.penup()
x_cor = -100
y_cor = -180
t.goto(x_cor,y_cor)

start = input('Press "s" to start the game')

x_change = 10
y_change = 10
screen.tracer(0)

def right():
  b1.forward(10)
  b2.forward(10)
  b3.forward(10)

def left():
  b1.backward(10)
  b2.backward(10)
  b3.backward(10)
  
screen.update()
if start == 's':
  while True:
    if x_cor > 260:
      x_change = -10
    elif x_cor < -260 :
      x_change = 10
    if y_cor > 200:
      y_change = -10
    elif y_cor < -170 :
      if b1.xcor()-x_cor <= 30 and b1.xcor()-x_cor >= -30 : 
        y_change = 10
      else:
        t.goto(x_cor,y_cor-20)
        print('You Lose!!')
        break
    x_cor = x_cor + x_change
    y_cor = y_cor + y_change
    t.goto(x_cor,y_cor)
    screen.onkey(right,'f')
    screen.onkey(left,'s')
    screen.listen()
    time.sleep(0.1)
    screen.update()
