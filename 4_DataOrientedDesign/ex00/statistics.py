def ft_statistics(*args: int, **kwargs: str) -> None:
    """def ft_statistics(*args: int, **kwargs: str)"""
    if (len(args) == 0):
        print("ERROR no number founded")
        return
    for key, value in kwargs.items():
        # Mean
        if (value == "mean"):
            print(f"Mean is {sum(args)/len(args)}")
        # Median
        elif (value == "median"):
            data = sorted(args)
            n = len(data)
            if (n % 2 == 1):
                print(f"Median is {data[n // 2]}")
            else:
                i = n // 2
                print(f"Median is {(data[i - 1] + data[i]) / 2}")
        # Quartile
        elif (value == "quartile"):
        # Standard Deviation
        elif (value == "std"):
        # Variance
        elif (value == "var"):


def main():
    ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
