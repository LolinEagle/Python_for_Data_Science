import sys


def main():
    if (len(sys.argv) != 2):
        print("Usage : python sos.py <string>")
        return (0)
    try:
        for i in sys.argv[1]:
            if (i.isalnum() is False and i.isspace() is False):
                raise AssertionError("AssertionError: the arguments are bad")
    except AssertionError as msg:
        print(msg)
        return (1)
    NESTED_MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
    }
    tmp = ""

    for i in sys.argv[1]:
        if (i.islower()):
            tmp += NESTED_MORSE[i.upper()]
        else:
            tmp += NESTED_MORSE[i]
    print(tmp)


if __name__ == "__main__":
    main()
