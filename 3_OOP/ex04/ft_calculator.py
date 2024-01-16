class calculator:
    """class calculator"""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """def dotproduct(V1: list[float], V2: list[float])"""
        V3 = 0
        i = 0
        while (i < len(V1) and i < len(V2)):
            V3 += V1[i] * V2[i]
            i += 1
        print(f"Dot product is: {V3}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """def add_vec(V1: list[float], V2: list[float])"""
        V3 = []
        i = 0
        while (i < len(V1) and i < len(V2)):
            V3.append(float(V1[i] + V2[i]))
            i += 1
        print(f"Add Vector is : {V3}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """def sous_vec(V1: list[float], V2: list[float])"""
        V3 = []
        i = 0
        while (i < len(V1) and i < len(V2)):
            V3.append(float(V1[i] - V2[i]))
            i += 1
        print(f"Sous Vector is: {V3}")


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
