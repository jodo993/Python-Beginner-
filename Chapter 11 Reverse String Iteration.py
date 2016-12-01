def reverse(text):
    reverse = ''
    for i in range(len(text)):
        reverse = reverse + text[len(text)-i-1]
    return reverse

def main():
    r = reverse("Hello!")
    print(r)
    print("Expected: !olleH")

main()
