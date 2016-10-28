# CSci 1133 HW 6
# Kayla Engelstad
# HW Problem 6A
# Lab Section 22

# SUDOKU CHECKER PROGRAM
# This program will pass a two dimensional list (9 rows, 9 columns) as an
# argument through the pure function named checkSudoku. checkSudoku will
# determine if the list represents a vaild solution to a Sudoku puzzle by making
# sure that each row, column, and subsquare contains only one of each integer
# from 1 through 9. If each check is validated, checkSudoku will return a
# boolean True. Boolean False will be returned if not all of the checks are
# validated. A unitTest prodcedure will call checkSudoku, displaying "Solution"
# or "Not Solution" when checkSudoku is called.

# define functions

def rowCheck(lst):
    # Boolean Flag
    solution = True

    for i in range(0, 9):
        numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # create a list for each row, and check each row
        rowList = list(lst[i])

        for k in range(len(rowList)):

            if rowList[k] in numlist:
                # remove val of rowList[k] from numlist
                val = numlist.index(rowList[k])
                numlist.remove(numlist[val])
                #print(numlist) -- for testing -- 

        if (numlist != []):
            solution = False

    return solution
    #print(solution) -- for testing --


def columnCheck(lst):
    # takes columns, makes thema appear as rows, then feeds them through rowCheck()
    colCount = 0
    newPuzzle = []

    for i in range(0, 9):
        # create a new column list before finding and checking next column.
        checkCount = 0
        colList = []

        for j in range(0, 9):
            colList.append(lst[j][colCount])
            #print(colList) -- for testing --
        newPuzzle.append(colList)
        #print(newPuzzle) -- for testing --
        colCount = colCount + 1

    result = rowCheck(newPuzzle)
    return result
    #print(result) -- for testing --

def squareCheck(lst):
    # takes squares, make them appear as rows, then feeds then through rowCheck()
    bigpuzzle = []

    for i in range(0, 9):
        squarevals = []
        nlist = i // 3 * 3

        for j in range(0, 9): 
            nitem = j // 3 * 3
        startsquare = lst[nlist][nitem]
        squarevals.append(startsquare)

        # row 1
        for k in range(0,2):
            nextItem = lst[nlist][nitem + (k + 1)]
            squarevals.append(nextItem)
            #print(squarevals) -- for testing --

        # row 2
        for l in range(0, 3):
            nextItem = lst[nlist + 1][nitem + l]
            squarevals.append(nextItem)
            #print(squarevals) -- for testing --

        # row 3
        for m in range(0, 3):
            nextItem = lst[nlist + 2][nitem + m]
            squarevals.append(nextItem)
            #print(squarevals) -- for testing --
        bigpuzzle.append(squarevals)
    #print(bigpuzzle) -- for testing --

    result = rowCheck(bigpuzzle)
    return result
    #print(result) -- for testing --

def checkSudoku(lst):
    if (rowCheck(lst) == True) and (columnCheck(lst) == True) and (squareCheck(lst) == True):
        return True
    else:
        return False

def unitTest():
    # test first example puzzle
    puzzle1 = [ [5, 3, 4, 6, 7, 8, 9, 1, 2], \
                [6, 7, 2, 1, 9, 5, 3, 4, 8], \
                [1, 9, 8, 3, 4, 2, 5, 6, 7], \
                [8, 5, 9, 7, 6, 1, 4, 2, 3], \
                [4, 2, 6, 8, 5, 3, 7, 9, 1], \
                [7, 1, 3, 9, 2, 4, 8, 5, 6], \
                [9, 6, 1, 5, 3, 7, 2, 8, 4], \
                [2, 8, 7, 4, 1, 9, 6, 3, 5], \
                [3, 4, 5, 2, 8, 6, 1, 7, 9]  ]
    
    result1 = checkSudoku(puzzle1)
    if result1 == True:
        print("Puzzle 1 is a solution.")
    else:
        print("Puzzle 1 is not a solution.")

    # test second example puzzle
    puzzle2 = [ [5, 3, 4, 6, 7, 8, 9, 1, 2], \
                [6, 7, 2, 1, 9, 5, 3, 4, 8], \
                [1, 9, 8, 3, 4, 2, 4, 6, 7], \
                [8, 5, 9, 7, 6, 1, 5, 2, 3], \
                [4, 2, 6, 8, 5, 3, 7, 9, 1], \
                [7, 1, 3, 9, 2, 4, 8, 5, 6], \
                [9, 6, 1, 5, 3, 7, 2, 8, 4], \
                [2, 8, 7, 4, 1, 9, 6, 3, 5], \
                [3, 4, 5, 2, 8, 6, 1, 7, 9]  ]
    
    result2 = checkSudoku(puzzle2)
    if result2 == True:
        print("Puzzle 2 is a solution.")
    else:
        print("Puzzle 2 is not a solution.")
    

# Greeting
print("Welcome to SUDOKU CHECKER PROGRAM.\n\nEnjoy the unitTest!\n\n")
unitTest()
