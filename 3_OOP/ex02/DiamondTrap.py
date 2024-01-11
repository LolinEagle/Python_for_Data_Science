from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """class King(Baratheon, Lannister)"""
    def __init__(self, first_name):
        """def __init__(self, first_name)"""
        Baratheon.__init__(self, first_name)

    def set_eyes(self, eyes):
        self.eyes = eyes

    def set_hairs(self, hairs):
        self.hairs = hairs

    def get_eyes(self):
        return (self.eyes)

    def get_hairs(self):
        return (self.hairs)


def main():
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
