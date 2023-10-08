four_suits = ['\u2660', '\u2665', '\u2666', '\u2663']

def simple_column(n):
    x = ''
    for suit in four_suits:
        x += f'\n{suit}'

    print(x * n)

def column_y_axis(n, m, text):

    x = ''
    for suit in four_suits:

        if text != None:
           x += '\n' + f'{suit}' + f' {text}'+ ((m-len(text)) * " ") + f'{suit}'
        else:
            x += '\n' + f'{suit}' + (m * ' ') + f'{suit}'

    print(n * x)


column_y_axis(2, 100, text='teste')