# CSci 1133 HW 7
# Kayla Engelstad
# HW Problem 7B
# Lab Section 22

# FIBONACCI PROGRAM
# Using recursion, FIBONACCI PROGRAM compute the Fibonacci number of a positive
# or negative integer.

# define function
def FibAny(num):

    # base case 1
    if num == 0:
        return 0

    # base case 2
    elif num == 1:
        return 1

    else:
        if (num < 0):
            fib = (-1)**(-num + 1) * (FibAny(-num - 1) + FibAny(-num - 2))
            return fib
        else:
            fib = (FibAny(num - 1) + FibAny(num - 2))
            return fib

# Greeting
print("Welcome to the FIBONACCI PROGRAM.\n")

# Get input
n = int(input("Enter any integer: "))
result = FibAny(n)
print(result)

