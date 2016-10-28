# CSci 1133 HW 3
# Kayla Engelstad
# HW Problem 3A
#
# Rock-Paper-Scissors
# Player 1 and Player 2 each enter R for rock, P for paper, or S for
# scissors. Rock-Paper-Scissors program will determine the winner according
# to these rules:
#                   R(rock) beats S(scissors)
#                   S(scissors) beats P(paper)
#                   P(paper) beats R(rock)
#
# Rock-Paper-Scissors will continue to run until players answer "N" to
# "Continue playing? Y/N"

# Greeting
print("Let's play ROCK-PAPER-SCISSORS!\nPlayers, input R for rock, P for")
print("paper, and S for scissors.\n\n")

# Boolean Flag
playing = True

# While loop that repeats game
while playing == True:
    # input check
    valid_input = False
    while valid_input == False:

        # obtain data from players 1 and 2
        p1 = input("Player 1: ").upper()
        p2 = input("Player 2: ").upper()

        # check inputs
        if (p1 in ("R", "P", "S")) and (p2 in ("R", "P", "S")):
            valid_input = True
        else:
            print("INVALID INPUT: Try again.")

    # decide winner using player input
    if (p1 == "R" and p2 == "S") or (p1 == "S" and p2 == "P") or (p1 == "P" and p2 == "R"):
        print("\nPlayer 1 wins!\n")
    elif p1 == p2:
        print("\nIt's a tie!\n")
    else:
        print("\nPlayer 2 wins!\n")

    #determine if user wants to continue
    q = input("Continue playing? Y/N: ").upper()

    # stop playing on "no"
    if q == "N":
        playing = False
    else:
        print("\n")

print("\nGoodbye!")

