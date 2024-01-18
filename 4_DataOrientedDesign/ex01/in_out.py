def square(x: int | float) -> int | float:
    """def square(x: int | float) -> int | float"""
    return (x * x)


def pow(x: int | float) -> int | float:
    """def pow(x: int | float) -> int | float"""
    return (x ** x)


def outer(x: int | float, function) -> object:
    """def outer(x: int | float, function) -> object"""
    def inner() -> float:
        """def inner() -> float"""
        nonlocal x
        x = function(x)
        return (x)
    return (inner)


def main():
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == "__main__":
    main()
