# This program reads a word and prints each character in a separate line

# Ask for a name
word = input("Please enter a word: ")

i = 0

# i less than length of word loop continues
while i  < len(word) :
    letter = word[i]
    print(letter)
    i = i + 1
