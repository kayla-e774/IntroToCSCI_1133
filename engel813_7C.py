# CSci 1133 HW 7
# Kayla Engelstad
# HW Problem 7C
# Lab Section 22

# BASE CONVERSION PROGRAM
# This program will convert a positive integer into any base (i.e. base 16, base
# 32) using convertBase function with the number and the intended base passed
# through convertBase as an argument.

# define function
def convertBase(num, base):
    LetterVals = [(10, "A"), (11, "B"), (12, "C"), (13, "D"), (14, "E"),
                  (15, "F"), (16, "G"), (17, "H"), (18, "I"), (19, "J"),
                  (20, "K"), (21, "L"), (22, "M"), (23, "N"), (24, "O"),
                  (25, "P"), (26, "Q"), (27, "R"), (28, "S"), (29, "T"),
                  (30, "U"), (31, "V"), (32, "W")]

    # base case
    if (num == 0):
        return str('')

    elif (num == 1):
        return str(1)

    else:

        # decide what the value is
        if (num % base) <= 9:
            val = str(num % base)
            #print(val)

        else:
            val = num % base
            val = val - 10
            val = LetterVals[val][1]
            print(val)

        # call convertBase to solve smaller problem and return answer
        return convertBase((num // base), base) + val


