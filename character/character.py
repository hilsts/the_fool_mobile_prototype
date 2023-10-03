from static.classes import CLASSES_EDGES, CLASSES
from world.world import World


class Character(World):

    def __init__(self, class_id, name):

        super().__init__()


        self.character_name = name
        self.character_id = self.create_character()
        self.class_ = CLASSES[class_id]

    def create_character(self):

        # TODO

        return 0
