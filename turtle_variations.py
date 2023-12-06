
import turtle
from turtle import *
import math, random

class bubble_turtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.pu()
        self.setpos(100,-100)
        self.pd()
    def fd (self,distance):
        segments = distance//10
        extra = distance%10
        for move in range(segments):
            self._go(10)
            self.circle(5)
        self._go(extra)

class wiggle_turtle(Turtle):
    ## This turtle wiggles instead of drawing straight lines when it moves forward with
    ## the fd method.
    
    ## This is the only difference between this turtle and typical members of Turtle
    def __init__(self):
        Turtle.__init__(self)
        self.pu()
        self.setpos(-100,100)
        self.pd()
    def fd (self,distance):
        degree_heading = math.radians(self.heading())
        x_distance = math.cos(degree_heading)*distance
        y_distance = math.sin(degree_heading)*distance
        up = True
        x_step = x_distance/20
        y_step = y_distance/20
        variation = 2
        for step in range(20):
            x,y = self.pos()
            if up:
                self.setposition(x+variation,y+y_step+variation)
                self.setposition(x+x_step-variation,y+y_step-variation)
            else:
                self.setposition(x+x_step-variation,y-variation)
                self.setposition(x+x_step+variation,y+y_step+variation)
            up = not(up)
            
class rainbow_turtle(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.pu()
        self.setpos(-100,0)
        self.pd()
    def fd(self,distance):
        self.randcolor()
        degree_heading = math.radians(self.heading())
        x_distance = math.cos(degree_heading)*distance
        y_distance = math.sin(degree_heading)*distance
        up = True
        x_step = x_distance/20
        y_step = y_distance/20
        for step in range(20):
            x,y = self.pos()
            self.randcolor()
            self.setposition(x+x_step,y+y_step)
    def randcolor(self):
            colorArray = ["red","green","goldenrod","blue","black","purple","thistle4"]
            self.color(colorArray[(random.randrange(7)-1)])

def test_turtles():
    ## make a test turtle and draw a triangle
    global adam1
    global adam2
    adam1 = rainbow_turtle()
    adam2 = rainbow_turtle()
    adam3 = rainbow_turtle()
    adam4 = rainbow_turtle()
    adam5 = rainbow_turtle()
    adam1.speed(0)
    adam2.speed(0)
    adam3.speed(0)
    adam4.speed(0)
    adam5.speed(0)
    adam1.penup()
    adam2.penup()
    adam3.penup()
    adam4.penup()
    adam5.penup()
    adam1.setpos(-100,100)
    adam2.setpos(100,-100)
    adam3.setpos(-100,-100)
    adam4.setpos(300,-100)
    adam5.setpos(-300,-100)
    adam1.pd()
    adam2.pd()
    adam3.pd()
    adam4.pd()
    adam5.pd()
    # adam1.pd()
    # adam2.pd()
    for num in range(3):
        adam1.fd(100)
        adam1.left(120)
    for num in range(4):
        adam2.fd(100)
        adam2.left(90)
    for num in range(5):
        adam3.fd(100)
        adam3.left(72)
    for num in range(6):
        adam4.fd(100)
        adam4.left(60)
    for num in range(7):
        adam5.fd(100)
        adam5.left(51.4)

test_turtles()
turtle.mainloop()
