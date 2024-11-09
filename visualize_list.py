import os

cell = '\u001b[42m \u001b[0m'

def visualize_list(lst):
    os.system('cls')
    max_height = max(lst)

    for i in range(max_height):
        for index, x in enumerate(lst):
            if x >= max_height - i:
                print(cell, end="")
            else:
                print(" ", end="")
            if index == len(lst) - 1:
                print()