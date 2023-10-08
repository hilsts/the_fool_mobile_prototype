from character.character import get_characters, Character
from world.world import World
import main_world

def input_validation(input, max_value):

    if input < 1 or input > max_value:
        return 0

    else:
        return 1

def load_game(character_id, characters):

    for char in characters:

            if char['character_id'] == character_id:

                world = World(world_id=char['world_id'])
                character = Character(world, character_id=character_id)




def list_characters():
    print("Choose a character: ")
    characters = get_characters()
    c = 1
    for character in characters:
        print(f"{c}. {character['character_id']},  {character['class_']}")
        c+=1
    input_ = input()
    if input_validation(int(input_), len(characters)):

        return load_charater()

    else:
        print("Valor inválido!")
        return list_characters()




