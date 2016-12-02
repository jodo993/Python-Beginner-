# This program reverses a string by using iteration

def reverse(text):
    # Start as empty string
    reverse = ''
    # Loop to add each char at a time backwards
    for i in range(len(text)):
        reverse = reverse + text[len(text)-i-1]
    return reverse

# Send string to function and display
def main():
    r = reverse("Hello!")
    print(r)
    print("Expected: !olleH")

# Start program
main()
