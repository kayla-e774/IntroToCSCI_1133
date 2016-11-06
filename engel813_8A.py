# CSci 1133 HW 8
# Kayla Engelstad
# HW Problem 8A
# Lab Section 22

# TEXT ANALYSIS PROGRAM
# This program will prompt the user for an input file and write results onto an output file as specified by the
# user. The program will find:
#
#   1) The number of characters in the document.
#   2) The number of words in the document.
#   3) The number of different (unique) words in the document.
#   4) A list of each word used in the document, with a count of how many times each word was used in
#      the document. The list should be sorted in ascending order (numerical frequency) (see example
#      below).
#   5) The number of sentences in the document.
#   6) The average word length for all words appearing in the file (including duplicates).
#   7) The number of words longer than 5 characters for all words appearing in the file (including
#      duplicates)

#   QUESTION: DOES RETURN COUNT AS A CHARACTER? (in this program, currently, it does.)


# define functions

def readFile(ifile_obj):
    file_string = ''
    count = 0
    # read input file and save as string (strip all tabs, /n characters, and make lowercase)
    for line in ifile_obj:
        count += 1
        print(line)
        string = line.strip('\n')
        string2 = string.strip(" ")
        string3 = string2.lower()
        print(string3) #--for testing

        if string3 != '':
            file_string = file_string + (string3 + ' ')
            print(file_string) #--for testing

    return (file_string, count)
            
def SentenceCount(filetext):
# SentenceCount function uses pieces and ideas from Dr. Challou's code.
    
    sentence_delimeters = ('.', '!', '?')
    sentencecount = 0
    reading_word = False

    for ch in filetext:
        if ch.isalpha() and not reading_word:
            reading_word = True
        else:
            if ch in sentence_delimeters:
                sentencecount = sentencecount + 1
    print(sentencecount) #--for testing
    return sentencecount

def listav(num_lst):
    sum1 = 0
    for i in range(len(num_lst)):
        sum1 = sum1 + num_lst[i]

    av = sum1 / (len(num_lst))
    print(av) #--for testing
    return av

def uniqueWord(word_list):
    same_words = []
    for i in range(len(word_list)):
        word = word_list[i]
        if (word_list.count(word) != 1) and (word not in same_words):
            same_words.append(word)

    print(same_words) #--for testing
    unique_count = len(word_list) - len(same_words)
    print(unique_count) #--for testing

    return (unique_count, same_words)

def SixAndUp(num_list):
    over_5 = 0
    for i in range(len(num_list)):
        if num_list[i] > 5:
            over_5 = over_5 + 1

    print(over_5) #--for testing
    return over_5

def ListWrite(ofile, slist, list1):
    nlist = list(list1)
    list2 = []

    for i in range(len(slist)):
        word = slist[i]
        for x in range(len(list1)):
            try:
                nlist.remove(word)
            except:
                continue

            print(nlist) #--for Testing
    
    for x in range(len(slist)):
        num = list1.count(slist[x])
        list2.append(num)
        print(list2) #--for testing

    ofile.write(format("Word List:", "^15") + format("Word Count:", "^20") + '\n')

    for i in range(len(nlist)):
        string = (format(nlist[i], "^15") + format("1", "^20") + '\n')
        print(string) #--for testing
        ofile.write(string)
    
    for i in range(len(slist)):
        string = (format(slist[i], "^15") + format(str(list2[i]), "^20") + '\n')
        print(string) #--for testing
        ofile.write(string)

def wordStuff2(filetext, lines):
    filetext = filetext.strip(' ')
    ch_count = 0
    punctuation = ",;:.\"'()?!"
    word_lengths = []
    
    # count characters
    for ch in filetext:
        if ch not in  ('\r', '\n'):
            ch_count = ch_count + 1
    ch_count = ch_count - (lines - 1)
    print(ch_count) #--for testing

    # count sentences
    s_count = SentenceCount(filetext)
           
    # remove punctuation
    for ch in filetext:
        if (ch in punctuation) or (ch.isdigit()):
            filetext = filetext.replace(ch, '')
    print(filetext) #--for testing

    # word count
    word_list = filetext.split(' ')
    #word_list.remove(word_list[len(word_list)-1])
    word_num = len(word_list)
    print(word_num) #--for testing

    # word lengths
    for i in range(len(word_list)):
        word_lengths.append(len(word_list[i]))
    print(word_lengths) #--for testing

    # average of word lengths
    av_length = listav(word_lengths)

    # lengths over 5
    over_5 = SixAndUp(word_lengths)

    # unique words
    num_unique, same_words = uniqueWord(word_list)

    
    return (ch_count, s_count, word_num, av_length, over_5, num_unique, same_words, word_list, word_lengths)
            
        
    

# -- main
# greeting
print("Welcome to TEXT ANALYSIS PROGRAM.\n")
print("This program will compute some statistics resulting from the analysis\nof the text in an input file you specify (e.g., myinputfile.txt) to\nan output file you specify (e.g., myoutputfile.txt)\n")

# get input
valid_file = False # flag
while not valid_file:
    input_file = input("Enter the name of the file which you wish to analyze (with extension): ")
    try:
        ifile_obj = open(input_file, "r")
        valid_file = True
    except:
        print("Input file not found - please re-enter.")
        valid_file = False

output_file = input("Enter the name of the file on which you wish to write results (with extension): ")
ofile_obj = open(output_file, "w")

# read input file and save as string (strip all tabs, /n characters, and make lowercase)
file_string, lines = readFile(ifile_obj)

# call functions/assign variables
ch_count, s_count, word_num, av_length, over_5, num_unique, same_words, word_list, word_lengths = wordStuff2(file_string, lines)

# write to output file
string1 = "File " + input_file + " contains:\n\n" + str(ch_count) + " character(s)\n" + str(word_num) + " word(s)\n" + str(num_unique) + " unique word(s)\n"
ofile_obj.write(string1)

ListWrite(ofile_obj, same_words, word_list)

string2 = "There is/are " + str(s_count) + " sentence(s) in the file " + input_file + "\nThe average word length is " + str(av_length) + " letter(s)\n" + "there is/are " + str(over_5) + " word(s) greater than 5 letters in length\n"
ofile_obj.write(string2)   


# close files
ifile_obj.close()
ofile_obj.close()
