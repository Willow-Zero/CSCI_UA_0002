# make the turtle graphics module available
import turtle

# set up our graphical canvas
# width = 500, height = 500
# starting point = 0, 0
turtle.setup(500,500,0,0)

# move the turtle forward by 100 pixels
# note that the turtle initially faces to the right
turtle.forward(100)

# now turn to the right by 90 degrees
turtle.right(90)

# now the turtle is facing down.  move another 100 pixels
turtle.forward(100)

# turn to the right by 90 more degrees
# this will point the turtle to the left
turtle.right(90)

# and move forward by another 100 pixels
turtle.forward(100)

# repeat the process one more time!
turtle.right(90)
turtle.forward(100)
