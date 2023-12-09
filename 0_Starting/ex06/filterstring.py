import sys


def main():
    if (len(sys.argv) < 3):
        print("Usage : python filterstring.py <string> <integer>")
        return (0)
    try:
        if (len(sys.argv) != 3):
            raise AssertionError("more than two argument is provided")
        try:
            av = int(sys.argv[2])
        except ValueError:
            raise AssertionError("argument is not an integer")
        ft_list = []
        tmp = ""

        for i in sys.argv[1]:
            if (i.isspace()):
                if (len(tmp) > av):
                    ft_list.append(tmp)
                tmp = ""
                continue
            tmp += i
        if (len(tmp) > av):
            ft_list.append(tmp)
        print(ft_list)
    except AssertionError as msg:
        print("AssertionError:", msg)
        return (1)


if __name__ == "__main__":
    main()
