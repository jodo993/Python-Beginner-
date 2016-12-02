# This program finds if a substring exist in a string using recursion

def find(text, string):
    # If first three char of text is same as substring, return true
    if text[0:3] == string:
        return True
    # If length of string is same as substring but no match is found, return False
    else:               
        if len(text) == len(string):
            return False
        else:
            # Remove first char of text
            text = text[1:]
            return find(text, string)

# Send the string and substring to check if sub exists in string
def main():
    print(find("Mississippi", "sip"))
    print("Excepted: True")

    print(find("Mississippi", "pip"))
    print("Expected: False")

# Start the program
main()
