from create import choose_class
from load import list_characters

def input_validation(input, max_value):

    if input < 1 or input > max_value:
        return 0

    else:
        return 1


def menu():

    print("\u2660 \u2665 \u2666 \u2663 THE FOOL - PROTOTYPE \u2660 \u2665 \u2666 \u2663")
    print("""
    1. Load
    2. New
    """)
    main_input = input()

    if input_validation(int(main_input), 2):
        if int(main_input) == 1:
            return list_characters()
        else:
            create = choose_class()
            return menu()
    else:
        print("Valor inválido")
        return menu()

menu()






