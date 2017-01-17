def main():
    print("Enter a sentence to count all E's")
    sentence = input("Enter sentence: ")

    countE(sentence)

def countE(sentence):
    sentence = sentence.lower()
    count = 0
    for char in sentence:
        if char in "e":
            count = count + 1
    return print("The sentence contains ", count, " e.")
main()
