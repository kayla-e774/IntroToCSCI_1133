# CSci 1133 HW 1
# Kayla Engelstad
# HW Problem 1A

# Here is a python program to convert the temperature in degrees Celsius from the temperature input by the user in Fahrenheit.
print('Hi! Welcome to the Fahrenheit to Celsius Temperature Conversion Program.')
Tf = float(input('Please enter the temperature in degrees Fahrenheit: '))
Tc = (Tf - 32) * (5/9)
print(Tc, ", is the temperature in degrees Celcius.")
# This is just my lame sense of humor, ignore it if you wish.
if Tc == 0:
    print("What's cooler than cool? ICE COLD!")
if Tc == 100:
    print('Take your pot off the stove, it is boiling!')
print('Have a nice day!')
