# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:16:08 2016

@author: Girish
"""

import turtle

# Create and set up screen and turtle.

t = turtle
# May need to tweak dimensions below for your screen.
t.setup(600, 600)
t.Screen()
t.title("Turtle Drawing Program - by Vasudev Ram")
t.showturtle()

# Set movement step and turning angle.
step = 160
angle = 45

def forward():
   
    t.forward(step)

def back():
    '''Move back step positions.'''
    t.back(step)

def left():
    '''Turn left by angle degrees.'''    
    t.left(1)

def right():
    '''Turn right by angle degrees.'''
    t.right(angle)

def home():
    '''Go to turtle home.'''
    t.home()

def clear():
    '''Clear drawing.'''
    t.clear()

def quit():
    t.bye()

t.onkey(forward, "Up")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.onkey(back, "Down")
t.onkey(home, "h")
t.onkey(home, "H")
t.onkey(clear, "c")
t.onkey(clear, "C")
t.onkey(quit, "q")
t.onkey(quit, "Q")

t.listen()
t.mainloop()