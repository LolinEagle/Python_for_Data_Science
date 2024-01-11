class calculator:
    """class calculator"""
    def __init__(self, data):
        self.data = data

    def __add__(self, object) -> None:
        i = 0
        while (i < len(self.data)):
            self.data[i] += object
            i += 1
        print(self.data)

    def __mul__(self, object) -> None:
        i = 0
        while (i < len(self.data)):
            self.data[i] *= object
            i += 1
        print(self.data)

    def __sub__(self, object) -> None:
        i = 0
        while (i < len(self.data)):
            self.data[i] -= object
            i += 1
        print(self.data)

    def __truediv__(self, object) -> None:
        if (object == 0):
            print("Error: Division by 0")
            return
        i = 0
        while (i < len(self.data)):
            self.data[i] /= object
            i += 1
        print(self.data)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5


if __name__ == "__main__":
    main()
