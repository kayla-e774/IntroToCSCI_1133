# CSci 1133 HW 2
# Kayla Engelstad
# HW Problem 2B
#
# This program will allow the user to draw and determine the side lengths of
# a hexagon. The hexagon will be drawn using turtle graphics.

# define procedure
def drawHexagon():

# open turtle
    import turtle
    turtle.showturtle()

# user determines side length of the hexagon
    side_length = float(turtle.textinput("Input Dialog", "Enter side length for the hexagon: "))

# draw six equal sides w/ interior angle of 60 degrees and colors in order:
# red, green, blue, yellow, purple, orange
    turtle.color('red')
    turtle.forward(side_length)
    turtle.right(60)
    turtle.color('green')
    turtle.forward(side_length)
    turtle.right(60)
    turtle.color('blue')
    turtle.forward(side_length)
    turtle.right(60)
    turtle.color('yellow')
    turtle.forward(side_length)
    turtle.right(60)
    turtle.color('purple')
    turtle.forward(side_length)
    turtle.right(60)
    turtle.color('orange')
    turtle.forward(side_length)
    turtle.right(60)

#call procedure
drawHexagon()
    
    
