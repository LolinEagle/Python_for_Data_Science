def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """def give_bmi(height: list[int | float], weight: list[int | float])"""
    if (type(height) is not list or type(height) is not list):
        print("Arguments need to be a list")
        return (0)
    if (len(height) != len(weight)):
        print("Number of height are not equal to the number of weight")
        return (0)
    i = 0
    bmi = []

    for h in height:
        bmi.append(weight[i] / (height[i] * height[i]))
        i += 1
    return (bmi)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """def apply_limit(bmi: list[int | float], limit: int)"""
    if (type(bmi) is not list):
        print("First arguments need to be a list")
        return (0)
    i = 0
    ft_list = []

    for b in bmi:
        ft_list.append(bmi[i] > limit)
        i += 1
    return (ft_list)


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)

    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
