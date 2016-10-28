# CSci 1133 HW 7
# Kayla Engelstad
# HW Problem 7A
# Lab Section 22

# LIST EQUALITY PROGRAM
# This program contains the recursive function isEqual to check whether two
# lists are equal by comparing the lengths of the lists and by testing whether
# the individual list elements are equal.

def isEqual(list1, list2):

    # base case
    if (len(list1) == 0) and (len(list2) == 0):
        print("The lists are equal!")
    else:
        if len(list1) != len(list2):
            print("The lists are not equal!")
        else:
            if list1[0] == list2[0]:
                isEqual(list1[1:], list2[1:])
            else:
                print("The lists are not equal!")


