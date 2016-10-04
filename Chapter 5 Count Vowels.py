# This program count the number of vowels in a word.

# Main function defintion
def main():
    # Ask user for input
    print("This program will tell you the vowels in a word.")
    word = input("Please enter a word: ")

    countVowels(word)   # Call countVowels function

# Finds the amount of vowels in the string
# @param string - The string where vowel will be counted
# @return - Display string
def countVowels(string):
    string = string.lower()
    count = 0
    for char in string:
        if char in "aeiou":
            count = count + 1
    return print("There are ", count, " vowels.")

# Calls the main function
main()
