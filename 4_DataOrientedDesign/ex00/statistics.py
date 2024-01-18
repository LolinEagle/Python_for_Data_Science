import numpy as np


def ft_statistics(*args: int, **kwargs: str) -> None:
    """def ft_statistics(*args: int, **kwargs: str)"""
    for key, value in kwargs.items():
        if (len(args) == 0):
            print("ERROR")
            continue
        if (value == "mean"):
            print(f"Mean is {np.mean(args)}")
        elif (value == "median"):
            print(f"Median is {np.median(args):.0f}")
        elif (value == "quartile"):
            quantile = np.quantile(args, [0.25, 0.75])
            print(f"Quartile is [{quantile[0]}, {quantile[1]}]")
        elif (value == "std"):
            print(f"Standard Deviation is {np.std(args)}")
        elif (value == "var"):
            print(f"Variance is {np.var(args)}")


def main():
    ft_statistics(1, 42, 360, 11, 64, a="mean", b="median", c="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, a="std", b="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, a="heheh", b="kdekem")
    print("-----")
    ft_statistics(a="mean", b="median", c="quartile")


if __name__ == "__main__":
    main()
