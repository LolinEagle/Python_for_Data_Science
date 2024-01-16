from abc import ABC, abstractmethod


class Character(ABC):
    """class Character(ABC)"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """def __init__(self, first_name, is_alive=True)"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """def die(self)"""
        self.is_alive = False


class Stark(Character):
    """class Stark(Character)"""
    def __init__(self, first_name, is_alive=True):
        """def __init__(self, first_name, is_alive=True)"""
        Character.__init__(self, first_name, is_alive)

    def die(self):
        """def die(self)"""
        Character.die(self)


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
