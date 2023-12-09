def NULL_not_found(object: any) -> int:
    object_type = type(object)
    object_dict = {
        None: "Nothing",
        float: "Cheese",
        int: "Zero",
        str: "Empty",
        bool: "Fake",
    }
    object_zero = object_dict.get(object_type)

    if (object and object_type != float):
        print("Type not found")
        return (1)
    if object_zero is None:
        print(f"Nothing: {object} {object_type}")
    else:
        print(f"{object_zero}: {object} {object_type}")
    return (0)
