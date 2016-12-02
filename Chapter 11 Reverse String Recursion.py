# This program reverses a string using recursion

def reverse(text):

    # Take first subscript out and add it last
    if len(text) <= 1:
        return text
    else:
        return reverse(text[1:]) + text[0]

# Send the string Hello to reverse function and display result
def main():
    r = reverse("Hello!")
    print(r)
    print("Expected: !olleH")

# Start program
main()
