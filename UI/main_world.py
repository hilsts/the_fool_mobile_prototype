from load import load_char_world, get_characters
from main_menu import menu


def world_menu():

    character_id = menu()
    characters = get_characters()
    world, character = load_char_world(character_id, characters)

    print(f"\u2660 \u2665 \u2666 \u2663 Welcome to World {world.world_id} \u2660 \u2665 \u2666 \u2663")

