from character.character import Character, get_characters
from world.world import World
from create import input_validation

def list_characters():
    print("Choose a character: ")
    characters = get_characters()
    c = 1
    for character in characters:
        print(f"{c}. {character['character_id']},  {character['class_']}")
        c+=1
    input_ = input()
    if input_validation(int(input_), len(characters)):

        return int(input_)

    else:
        print("Valor inválido!")
        return list_characters()

def load_char_world(character_id, characters):

    for char in characters:

        if char['character_id'] == character_id:

            world = World(world_id=char['world_id'])
            character = Character(world)
            character.load_character(char)

            # print(character.__dict__)
            return [world, character]

#
# def load_mechanics(class_id):
#
#     # TODO


