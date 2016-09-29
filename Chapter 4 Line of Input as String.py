# This program read a line of input and print
# Uppercase, second letter, vowel replaced by underscore

# Print uppercase
sentence = input("Enter a line: ")
print("Uppercase letter of String")
for i in range(len(sentence)) :
    if sentence[i].isupper() :
        print(sentence[i])

# Print every 2nd letter of string
print()
print("Second Letter of String")
even = 2
for j in range(len(sentence)) :
    if even % 2 != 0 :
        print(sentence[j])
        even = even + 1
    else:
        even = even + 1

# Print vowels replaced with underscore
print()
print("Replacing vowels with underscore in String")
for char in sentence :
    if char in "aeiou" :
        sentence = sentence.replace(char, '_')
print(sentence)
