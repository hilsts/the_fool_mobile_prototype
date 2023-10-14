from static.classes import CLASSES_EDGES, CLASSES
from world.world import World
from data import data_handler

CHARACTERS_PATH = "../data/character/characters.json"
CHARACTER_PATH = "../data/character/character.json"


class Character(World):


    def __init__(self, *args):

        self.__dict__ = args[0].__dict__.copy()


    def load_character(self, character_obj):

        for key in character_obj.keys():
            self.__dict__[key] = character_obj[key]


    def create_character(self, class_id):


        self.class_id = class_id
        self.class_ = CLASSES[class_id]


        if data_handler.verify_path_exists(CHARACTERS_PATH):

            characters = data_handler.get_file_data(CHARACTERS_PATH)
            character = data_handler.get_file_data(CHARACTER_PATH)
            self.character_id = characters[-1]+1


            characters.append(self.character_id)
            character.append(self.__dict__)

            data_handler.create_file_from_data(characters, CHARACTERS_PATH)
            data_handler.create_file_from_data(character, CHARACTER_PATH)

        else:
            self.character_id = 0
            characters = [0]
            data_handler.create_file_from_data(characters, CHARACTERS_PATH)

            character = [self.__dict__]
            data_handler.create_file_from_data(character, CHARACTER_PATH)

def get_characters():

    characters = data_handler.get_file_data(CHARACTER_PATH)

    return characters




