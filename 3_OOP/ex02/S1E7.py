from S1E9 import Character


class Baratheon(Character):
    """class Baratheon(Character)"""
    def __init__(self, first_name, is_alive=True, family_name="Baratheon",
                 eyes="brown", hairs="dark"):
        """def __init__(self, first_name, is_alive=True)"""
        Character.__init__(self, first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """def die(self)"""
        Character.die(self)


class Lannister(Character):
    def __init__(self, first_name, is_alive=True, family_name="Lannister",
                 eyes="blue", hairs="light"):
        """def __init__(self, first_name, is_alive=True)"""
        Character.__init__(self, first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def create_lannister(first_name, is_alive=True):
        return (Lannister(first_name, is_alive))


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : \
{Jaine.is_alive}")


if __name__ == "__main__":
    main()
