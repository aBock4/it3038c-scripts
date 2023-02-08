#Friendly message explaining what the program will do
print('This program will count how many letters, vowels, and consonants there are in a provided word')

#Take in a word as input with friendly message
print('Please type a word')

#Assign input to a variable
word = input()

#Function to count letters in the word
def countLetters(word):
    #set a counter
    count = 0
    #iterate through the word with for loop
    for c in word:
        #add 1 when iterated through
        count += 1
    result = ("There are " + str(count) + " letters.")
    return result

#Function to count vowels/consonants in the word
def countVowelsAndConsonants(word):
    #set variable to hold vowel number
    vowels = 0;
    #set variable to hold consonant number
    consonants = 0;
    #for loop to iterate through the word
    for c in word:
        #set each letter to lowercase
        letter = c.lower()
        #if letter ie a,e,i,o, or u add 1 to vowel
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            vowels += 1
        #else add 1 to consonant
        else: 
            consonants += 1
    #return the number of vowels and consonant in friendly message
    result = ("There are " + str(vowels) + " vowels and " + str(consonants) + " consonants")
    return result

#use countLetters function to count letters     
number = countLetters(word)

#print the result
print(number)

#use countVowelsAndConsonants function to count letters
test = countVowelsAndConsonants(word)

#print the result
print(test) 