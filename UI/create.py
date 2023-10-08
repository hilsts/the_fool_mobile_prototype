from static.classes import CLASSES, SUITS_CLASSES
from world.world import World
from character.character import Character, get_characters

SEASONS = {
    "winter",
    "summer",
    "spring",
    "autumn"
}

def generate_start_date():
    return 0
def simulate_year(n_days):
    return 0


def input_validation(input, max_value):

    if input < 1 or input > max_value:
        return 0

    else:
        return 1

def suit_input():

    suit_id = input()

    if input_validation(int(suit_id), 4):

        return int(suit_id)
    else:
        print("Valor inválido")
        return suit_input()

def class_input():

    class_id = input()

    if input_validation(int(class_id), 2):

        return int(class_id)
    else:
        print("Valor inválido")
        return class_input()


def choose_suit():

    print("Choose your nation:")
    suits = list(SUITS_CLASSES.keys())
    for suit in suits:


        print(f"{suits.index(suit)+1}. {suit}")

    suit_id = suit_input()

    return suit_id

def choose_class():

    world = World()
    world.create_world()



    suits = list(SUITS_CLASSES.keys())
    suit_id = choose_suit()
    suit = suits[suit_id-1]
    suit_classes = SUITS_CLASSES[suit]
    print("Now, choose a class to start in this nation:")
    c = 1
    for class_ in suit_classes:

        print(f"{c}. {class_}")
        c+=1

    suit_class_id = class_input()
    class_id = CLASSES.index(suit_classes[suit_class_id-1])

    character = Character(world)
    character.create_character(class_id=class_id)

    print(f"class_id: {class_id}")
    return 0


def list_characters():
    print("Choose a character: ")
    characters = get_characters()
    c = 1
    for character in characters:

        print(f"{c}. {character['character_id']},  {character['class_name']}")

    input_ = input()
    if input_validation(input_, len(characters)):
        return



