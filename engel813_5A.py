# CSci 1133 HW 5
# Kayla Engelstad
# HW Problem 5A

# TEST SCORE STATISTICS PROGRAM
# This program will allow the user to input any number of test scores and
# return the number of scores entered, maximum score, minimum score,
# average score, and the standard deviation (using provided equation) of the
# scores. The user will beable to terminate the program and calculate the
# scores by entering a negative number.

# Functions
def getscores():
    # Boolean Flag
    entering = True
    # Create empty list to store scores
    scorelist = []
    while entering:
        scoreStr = input("Please enter a score from 0-100 or enter a negative\nnumber to compute results: ")
        # attempt to make input an integer, if failed, print error message, then continue
        try:
            score = int(scoreStr)
        except:
            print("INVALID INPUT: Please try again.")
            continue
        # make input an integer value
        score = int(scoreStr)
        # Choose what to do with int value of score
        if score < 0:
            entering = False
        elif (score > 100):
            print("INVALID INPUT: Please try again.")
        else: 
            scorelist.append(score)


    return scorelist
            
def min_score(lst):
    smallest = lst[0]
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest

def max_score(lst):
    largest = lst[0]
    for i in range(len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest

def av_score(lst):
    total = 0
    for i in range(len(lst)):
        total = total + lst[i]
    av = total / len(lst)
    return av

def deviation(lst):
    sum1 = 0
    av = av_score(lst)
    for i in range(len(lst)):
        sum1 = sum1 + ((lst[i] - av) ** 2)
    dev = ((1 / len(lst)) * sum1) ** .5
    return dev

# Greeting
print("Welcome to the TEST SCORE STATISTICS PROGRAM.\n")

# Termination Loop
running = True
while running:
    # main execution sequence
    # initialize list
    slist = []
    # call functions and assign results to variables
    slist = getscores()
    smallest = min_score(slist)
    largest = max_score(slist)
    average = av_score(slist)
    deviation = deviation(slist)
    # print results in statements
    print(slist)
    print("Number of scores: ", len(slist))
    print("Highest score: ", largest)
    print("Lowest score: ", smallest)
    print("Average of scores: ", average)
    print("Deviation of scores: ", deviation)

    # ask to continue
    answer = input("Would you like to run TEST SCORE STATISTICS PROGRAM again? (Y/N): ").upper()
    if answer == "N":
        running = False

print("\nGoodbye!\n")
    
