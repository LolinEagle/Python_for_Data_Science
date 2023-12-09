import sys


def main():
    try:
        if (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
    except AssertionError as msg:
        print("AssertionError:", msg)
        return (1)
    if (len(sys.argv) < 2):
        av = input("What is the text to count?\n")
    elif (len(sys.argv[1]) == 0):
        av = input("What is the text to count?\n")
    else:
        av = sys.argv[1]
    char = 0
    upper = 0
    lower = 0
    marks = 0
    spaces = 0
    digits = 0

    for i in av:
        char += 1
        if (i.isupper()):
            upper += 1
        elif (i.islower()):
            lower += 1
        elif (i.isspace()):
            spaces += 1
        elif (i.isdecimal()):
            digits += 1
        else:
            for j in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
                if (i == j):
                    marks += 1
    print(f"The text contains {char} characters:\n\
{upper} upper letters\n\
{lower} lower letters\n\
{marks} punctuation marks\n\
{spaces} spaces\n\
{digits} digits")


if __name__ == "__main__":
    main()
