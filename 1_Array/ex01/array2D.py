import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """def slice_me(family: list, start: int, end: int)"""
    try:
        if not (isinstance(family, list)):
            raise TypeError("Family must be a list")
        if not all(isinstance(sublist, list) and
                   len(sublist) == len(family[0]) for sublist in family):
            raise ValueError("All sublists must be a list and of the same len")
        arr = numpy.array(family)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return
    ret = family[start:end]
    print(f"My shape is: {arr.shape}")
    print(f"My new shape is: {numpy.array(ret).shape}")
    return (ret)


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2],]

    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
