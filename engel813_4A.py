# CSci 1133 HW 4
# Kayla Engelstad
# HW Problem 4A
#
# SINE COMPUTATION PROGRAM
# This program will take a degree input from the user, convert the degree to
# radians, then compute sine using:
#
#       sin x = x − x^3/3! + x^5/5! − x^7/7! + x^9/9! − …

#
# The program will end the computation according to a tolerance obtained
# from the user. It will aslo check for invalid inputs and will terminate
# when the user no longer wants to compute another number.
#
# Questions: inequality values for tolerance correct?

# Greeting
print("Welcome to the SINE COMPUTATION PROGRAM. Kiss your trig worries goodbye!\n")

# Define functions
def radian(num):
    pi = 3.1415926535
    r = num * ((2 * pi) / 360)
    return r

def factorial(num):
    results = 1
    while (num >= 1):
        results = results * num
        num = num - 1
    return results

def sine(num, tol):
    # set variables for use in loop
    n = -1 # for alternating addition and subtraction
    e = 3 # exponent/denominator
    d = factorial(3)
    current_val = num
    next_val = current_val + ((n / d) * pow(num, e))
    
    # while loop with tolerance considered
    while (n * (next_val - current_val) > tol):
        n = n * (-1) # alternate +/-
        e = e + 2 # raise numerator and denominator by 2
        d = factorial(e) # denominator
        current_val = next_val
        next_val = current_val + ((n / d) * pow(num, e))
    return next_val
        
def getangle():

    # angle input Flag and while loop
    valid_angle = False
    while not valid_angle:

        # get angle from user
        angle = float(input("Enter the measure of the angle you wish to compute: "))

        # check input
        if (angle < 0) or (angle > 360):
            print("INVALID INPUT: Please input an angle measurement betweem 0 and 360.")
        else:
            valid_angle = True
            return angle

def getTolerance():

    # tolerance input Flag and while loop
    valid_tolerance = False
    while not valid_tolerance:

        # get tolerance from user
        tolerance = float(input("Please enter tolerance for decimal accuracy (ex. .001, .1, .01, etc.): "))

        # check input
        if (tolerance <= 0) or (tolerance > 1):
            print("INVALID INPUT: The tolerance must be greater than 0 and no greater than 1.")
        else:
            valid_tolerance = True
            return tolerance

# Boolean Flag and while loop
program_run = True
while program_run:

    # call / assign "get" functions
    tolerance = getTolerance()
    angle = getangle()

    # convert angle to radians
    rad = radian(angle)

    # compute sine according to tolerance / show results
    result = sine(rad, tolerance)
    print("\nThe sine of", angle, "degrees is:", result)

    # ask to exit program
    stop = input("\nWould you like to compute sine again? (Y/N): ").upper()

    # selection to exit
    if stop == "N":
        program_run = False

print("\nGoodbye and good luck!")
