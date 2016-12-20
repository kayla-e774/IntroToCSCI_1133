# CSci 1133 HW 9
# Kayla Engelstad
# HW Problem 9A
# Lab Section 22

# WORDS TO NUMBERS PROGRAM
# This program will prompt a user to enter a telephone number containing letters and output the equivalent telephone
# number containing only digits. This program will work for 7 digit or 10 digit phone numbers and will terminate
# when the user enters a null string. The getNum() function will be inpure while the convertNum() function will be
# pure.

# define functions
def getNum():
    #choice = True
    numstring = ''
    alpha_num = input("Enter a 7 or 10 digit telephone number (entering an empty line will exit the program): ")

    if alpha_num != '':
        
        for ch in alpha_num:
            if ch.isalpha() or ch.isdigit():
                numstring += ch
                #print(numstring) #--for testing

    #print(numstring)#--for testing
    #print(len(numstring)) #--for testing
    #print(choice) #--for testing


    return (numstring)


def convertNum(string):
    string = string.upper()
    newNum = ''
    keys = sorted(letters_dictionary.keys())
    #print(keys) #--for testing

    for ch in string:
        if ch.isalpha():
            for i in range(len(keys)):
                if ch in keys[i]:
                    ch = letters_dictionary[keys[i]]
                    newNum = newNum + str(ch)
        else:
            newNum = newNum + str(ch)

    
    #print(newNum) #--for testing
    return newNum


# -- main
print("Welcome to WORDS TO NUMBERS PROGRAM.\n")

running = True # flag
while running:
    letters_dictionary = {('A', 'B', 'C'): 2, ('D', 'E', 'F'): 3, ('G', 'H', 'I'): 4, ('J', 'K', 'L'): 5,
                          ('M', 'N', 'O'): 6, ('P', 'Q', 'R', 'S'): 7, ('T', 'U', 'V'): 8, ('W', 'X', 'Y', 'Z'): 9}
    num = getNum()
    #print("return from getNum:", num, len(num)) #--for testing
    
    if num == '':
        running = False
        #print("Should be False:", running) #--for testing

    else:
        answer_num = convertNum(num)

        if (len(answer_num) == 7):
            answer_string = answer_num[0:3] + '-' + answer_num[3:]
            print("Numeric Telephone Number is: ", answer_string)

        elif (len(answer_num) == 10):
            answer_string = answer_num[0:3] + '-' + answer_num[3:6] + '-' + answer_num[6:]
            print("Numeric Telephone Number is: ", answer_string)

        else:
            print("The phone number you entered is not in the correct 7 or 10 digit form. Please try again.") 

    num = ''

    #print("Got here", running) #--for testing

print("Goodbye!")
        
        
