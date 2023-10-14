from character.character import Character

MECHANIC_PATH = "../data/mechanic/mechanic.json"

class Mechanic(Character):

    def __init__(self, *args):

        super().__init__(*args)


    def build_mechanic(self, start):

        print(self.__dict__)

