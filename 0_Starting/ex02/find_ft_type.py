def all_thing_is_obj(object: any) -> int:
    object_type = type(object)
    object_dict = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "Brian is in the kitchen",
    }

    if object_type == int:
        print("Type not found")
    else:
        print(f"{object_dict[object_type]} : {object_type}")
    return (42)
