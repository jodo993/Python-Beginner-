# This program reverses a word
def main():

    # User input and send to method
    word = input("Enter a word: ")
    print(reverse(word))

#@param word - word that user inputted
#@param return - return the word with commas
def reverse(word): 
    begin = 0 
    end = len(word) - 1 
    strlist = [i for i in word]

    # Reverse the word by using a holder to hold the first and switching
    # around the letter
    while(begin < end): 
        temp = strlist[begin]
        strlist[begin] = strlist[end] + ","
        strlist[end] = "," + temp
        begin += 1 
        end -= 1 
    return ''.join(strlist)

# Start program
main()
