# CSci 1133 HW 3
# Kayla Engelstad
# HW Problem 3B
#
# Installment Loan Program
# Using the equations:
#                       I = PRT and F = P + I
# Where variables P = the amount of principal the customer wants to borrow,
# R = interest rate, and T = term / time user needs to pay back the loan are
# retrieved from the user to calculate I (interest). I and P are then used
# to calculate F (face value). Lastly, a monthly payment, Mpay, is
# calculated when F is divided by 12.
#
# Invalid points to check for:
#       R: must be >0% and <= 20%
#       T: must be in years also >0 and <=5
#       P: must be >0

# Greeting
print("Welcome to the installment loan evaluation program!\n")

# while loop encompassing whole program:
running = True

# Get iinput from user
P = float(input("Please input the amount of money you will be borrowing: "))

        # check input / Terminate
if (P <= 0):
        print("Invalid Input: The amount borrowed must be greater than zero.")
        running = False

if running == True:
        # Get input from user
    R = float(input("Please input the interest rate (no % symbol necessary): "))

        # check input
    if (R <= 0) or (R > 20):
            print("Invalid Input: The interest rate must be a POSITIVE number that is \nno greater than 20.")
            running = False
    else:
            # Convert R to percentage
            R = R * .01
            print(R)

if running == True:
        # Get input from user
    T = float(input("Please input the term for the loan (in years): "))

        # check input
    if (T <= 0) or (T > 5):
            print("Invalid Input: The term must be a POSITIVE value that is \nno greater than 5 years.")
            running = False
    else:

            # Convert T (years) to months.
            T_months = T * 12

if running == True:
    # Calculate Interest
    I = P * R * T

    # Calculate Face Value
    F = I + P

    # Calculate Monthly Payment
    Mpay = F / T_months

    #Print results for user
    print("The face valure of the loan is: $", format(F, ".2f"))
    print("The monthly paymenr for the loan is: $", format(Mpay, ".2f"))

    #Continue?
    ask = input("Would you like to run this program again? (Y/N): ").upper()
    if ask == "N":
        running = False
        print("\nGoodbye.")
