import turtle as t
import math as m
import random as r
t.colormode(255)

def body(color,width):
    t.up()
    t.goto(0,-100)
    t.down()
    t.left(90)
    t.color(color)
    t.width(width)
    t.forward(200)
    
def head(type):
    i=0
    type += 1
    t.right(90)
    print(type)
    if type == 1:
        t.circle(50)
    if type == 2:
        t.forward(50)
        while i<=type:
            t.left(120)
            t.forward(100)
            i+=1
        t.backward(50)
    if type == 3:
        t.forward(45)
        t.left(90)
        t.forward(90)
        t.left(90)
        t.forward(90)
        t.left(90)
        t.forward(90)
        t.left(90)
        t.forward(45)
    if type == 4:
        t.forward(30)
        t.left(60)
        t.forward(60)
        t.left(60)
        t.forward(60)
        t.left(60)
        t.forward(60)
        t.left(60)
        t.forward(60)
        t.left(60)
        t.forward(60)
        t.left(60)
        t.forward(30)        
    if type == 5:
        t.circle(r.randrange(30)+35)
    if type == 6:
        t.up()
        t.left(90)
        t.forward(60)
        t.left(90)
        t.down()
        angle = (180-25.714)
        t.left(angle/2)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle/2)
    if type == 7:
        angle = (180-25.714)
        t.left(angle/2)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle)
        t.forward(90)
        t.left(angle/2)

 



def arm(angle1,angle2,l):
    t.up()
    t.goto(0,0)
    t.down()
    t.seth(270)
    if l == True:
        angle1 += 180
    t.left(angle1)
    t.forward(75)
    t.left(angle2)
    t.forward(75)



def leg(angle1,angle2,l):
    t.up()
    t.goto(0,-100)
    t.down()
    t.seth(270)
    if l == True:
        angle1 += 270
    t.left(angle1)
    t.forward(75)
    t.left(angle2)
    t.forward(75)
r.seed()
body((r.randrange(256),r.randrange(256),r.randrange(256)),r.randrange(10))
head(r.randrange(7))
leg((r.randrange(75)+15),(r.randrange(90)-45),False)
leg((r.randrange(75)+15),(r.randrange(90)-45),True)
arm((r.randrange(90)+45),(r.randrange(90)-45),False)
arm((r.randrange(90)+45),(r.randrange(90)-45),True)

t.mainloop()
