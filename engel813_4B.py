# CSci 1133 HW 4
# Kayla Engelstad
# HW Problem 4B
#
# DUAL DRAW PROGRAM
# This program allow the user to choose either squares or triangles to draw
# in a 360 degree arc around a turtle graphics canvas. The user will be able
# to control the number of shapes drawn with the proper input of an integer
# value.
#
# Question: Should I truncate division for numbers that don't go evenly into 360?

# Greeting
print("Welcome to DUAL DRAW PROGRAM. Create amazing patterns using triagles or squares!")

# import turtle library
import turtle

# define functions
def drawsquare(num, degree):
    turtle.showturtle()
    turtle.color('red')
    turtle.forward(num)
    turtle.right(90)
    turtle.forward(num)
    turtle.right(90)
    turtle.forward(num)
    turtle.right(90)
    turtle.forward(num)
    turtle.right(degree)
    
    

def drawtriangle(num, degree):
    turtle.showturtle()
    turtle.color('blue')
    turtle.forward(num)
    turtle.right(120)
    turtle.forward(num)
    turtle.right(120)
    turtle.forward(num)
    turtle.right(degree)

def shape_input():
    # shape input flag and while loop
    valid_shape = False
    while not valid_shape:

        # Get user input
        shape = input("Would you like to draw a triangle or square?: ").upper()

        # check input
        if shape not in ("TRIANGLE", "SQUARE"):
            print("INVALID INPUT: Please choose either 'triangle' or 'square'.")
        else:
            valid_shape = True
            return(shape)

def num_input():
    # number input flag and while loop
    valid_num = False
    while not valid_num:

        # Get user input
        num1 = int(input("How many shapes would you like to draw?: "))

        # Check input
        if (type(num1) == float) or (type(num1) == str) or (num1 <= 0):
            print("INVALID INPUT: Please enter a positive integer value.")
        else:
            valid_num = True
            return(num1)

# Boolean Flag and while loop
program_run = True
while program_run:
    c = 0 # loop count
    side = 50 # side length of all shapes
    num1 = num_input()
    shape = shape_input()

    #find degrees of rotation between each shape
    degrees = 360 / num1
    total_degrees = 0

    # while loop to control drawing
    while (total_degrees < 360):
        
        # decide to draw triangle or square
        if shape == "TRIANGLE":
            drawtriangle(side, degrees)
        else:
            drawsquare(side, degrees)
        total_degrees = total_degrees + degrees # track position relative to 360
        c = c + 1 # add to loop count
    

            
