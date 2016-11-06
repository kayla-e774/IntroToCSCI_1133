# CSci 1133 HW 8
# Kayla Engelstad
# HW Problem 8B
# Lab Section 22

# ENCRYPTION AND DECRYPTION PROGRAM
# This program will allow a user to either encrypt or decrypt a file based on a key in the file cipher.txt. If the
# user chooses to encrypt, the file will be scrambled according to cipher.txt, and the encryption will be printed
# in a file with the extention ".ecr". If the user chooses to decrypt, the encrypted file will be unscrambled using
# cipher.txt, and the the decryption will be stored in a file with the extension ".txt".

# define functions
def makeCipherLists():
    ListKey = []
    ListAlpha = []
    cipher = open("cipher.txt")
    alpha = cipher.readline()
    print(alpha) #--for testing
    key = cipher.readline()
    print(key) #--for testing

    for i in range(len(alpha) - 1):
        ListAlpha.append(alpha[i])
        ListKey.append(key[i])
        
    print(ListAlpha) #--for testing
    print(ListKey) #--for testing

    cipher.close()
    return (ListAlpha, ListKey)

def encrypt(ifile_obj, ListAlpha, ListKey):
    answer_string = ''
    for ch in ifile_obj:
        if ch in ListAlpha:
            val = ListAlpha.index(ch)
            print(val)
            answer_string += ListKey[val]
        else:
            answer_string += ch


    print(answer_string) #--for testing
    return answer_string


def decrypt(ifile_obj, ListAlpha, ListKey):
    answer_string = ''
    for ch in ifile_obj:
        if ch in ListKey:
            val = ListKey.index(ch)
            print(val)
            answer_string += ListAlpha[val]
        else:
            answer_string += ch


    print(answer_string) #--for testing
    return answer_string


def getInput():
    valid_input = False
    while not valid_input:
        ifile = input("Enter the name of a text file with extension: ")
        try:
            ifile_obj = open(ifile)
            valid_input = True
        except:
            print("Error retrieving file for reading, please try entering the file name again.\n")

    valid_choice = False
    while not valid_choice:
        answer = input("Do you wish to encrypt or decrypt this file (Enter 'E' or 'D'): ").upper()

        if answer in ("E", "D"):
            valid_choice = True
            
        else:
            print("Invalid Input, please enter 'E' or 'D'.")

    return(answer, ifile, ifile_obj)

# greeting
print("Welcome to ENCRYPTION AND DECRYPTION PROGRAM.\n")

running = True
while running:

    answer, ifile, ifile_obj = getInput()

    ListAlpha, ListKey = makeCipherLists()

    if answer == "E":
        naming = ifile.split(".")
        ofile = naming[0] + ".ecr"
        print(ofile) #--for testing
        ofile_obj = open(ofile, "w")
        answer_string = encrypt(ifile_obj, ListAlpha, ListKey)
        ofile_obj.write(answer_string)

    if answer == "D":
        naming = ifile. split(".")
        ofile = naming[0] + ".txt"
        print(ofile) #-- for testing
        ofile_obj = open(ofile, "w")
        answer_string = decrypt(ifile_obj, ListAlpha, ListKey)
        ofile_obj.write(answer_string)


    # close files
    ofile_obj.close()
    ifile_obj.close()

    again = input("Would you like to run ENCRYPTION AND DECRYPTION PROGRAM again? (Y/N): ").upper()

    if again == "N":
        running = False

print("\n\nGoodbye!")
