# CSci 1133 HW 5
# Kayla Engelstad
# HW Problem 5B

# SUBSTRING COUNTER PROGRAM
# This program will allow the user to input a string and a substing and
# shows how many times the substring occurs in the larger, primary string.

# Functions
def subStringCount(substr, fullstr):
    count = 0
    for i in range(len(fullstr)):
        if fullstr[i] == substr[0]:
            checkstring = fullstr[i:(i + len(substr))]
            if checkstring == substr:
                count = count + 1
    return count
                

# Greeting
print("Welcome to the SUBSTRING COUNTER PROGRAM.")

# termination loop
running = True
while running:
    # get user input
    string = str(input("Please enter a string: "))
    substring = str(input("Please enter a substring: "))

    # get/display results
    results = subStringCount(substring, string)
    print("The substring appears", results, "times in the string.")

    # run again?
    answer = input("Would you like to run this program again? (Y/N): ").upper()
    if answer == "N":
        running = False

print("\nGoodbye!\n")
