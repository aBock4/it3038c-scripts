#Friendly message explaining what the program will do
print('This program will count how many letters, vowels, and consonants there are in a provided word')

#Take in a word as input with friendly message
print('Please type a word')

#Assign input to a variable
word = input()

#Function to count letters in the word
def countLetters(word):
    #set a counter
    dict = 0
    #iterate through the word with for loop
    for c in word:
        #add 1 when iterated through
        dict += 1
    return dict

#Function to count vowels/consonants in the word
def countVowelsAndConsonants(word):
    vowels = 0;
    consonants = 0;
    for c in word:
        if c == "a" or "e" or "i"or "o"or "u":
            vowels += 1
        else: 
            consonants += 1
    return ('There are ' + int(vowels) + " vowels and " + consonants + " consonants.")
     
number = countLetters(word)
print(number)

test = countVowelsAndConsonants(word)
print(test) 