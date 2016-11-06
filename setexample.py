# Kayla Engelstad
# ID; 5245863
# Lab Section 22

def countVC(string):
    vowel_count = 0
    consonant_count = 0
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    for ch in string:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return(vowel_count, consonant_count)

word = input("Enter a string of letters: ").lower()
vowel_num, consonant_num = countVC(word)
print("There are ", vowel_num, " vowels in the string.")
print("There are ", consonant_num, " cononants in the string.")
