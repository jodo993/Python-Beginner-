def find(text, string):
    if text[0:3] == string:
        return True
    else:
        if len(text) == len(string):
            return False
        else:
            text = text[1:]
            return find(text, string)

def main():
    print(find("Mississippi", "sip"))
    print("Excepted: True")

    print(find("Mississippi", "pip"))
    print("Expected: False")

main()
