from character.character import Character
from mechanic.mechanic import Mechanic


MINE_START = {
    "level" : 1,
    "level_per_hour" : 5,
    "quant_per_level" : 0.1,
    "resource_class" : 1,
    "resource_class_per_level" : 0.01
}


class Mine(Character, Mechanic):

    def __init__(self, class_id, name):
        super().__init__(class_id, name)

        self.mechanic_name = "mine"


        self.build_mechanic(MINE_START)



character = Character(class_id=0, name='teste')
mechanic = Mechanic()
mine = Mine(character.character_id, character.character_name)



