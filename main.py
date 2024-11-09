import os
import random
from algorithms.boggo import boggo_sort
from algorithms.bubble import bubble_sort
from algorithms.merge import merge_sort
from algorithms.insertion import insertion_sort_gpt

cell = '\u001b[42m \u001b[0m'


def generate_list(count):
    lst = [None] * count
    num = 1
    for i in range(count):
        lst[i] = num
        num += 1
    random.shuffle(lst)
    return lst

def execute_boggo_sort(lst):
    sorting_time = boggo_sort(lst, sorted(lst))
    print('List sorted in:',sorting_time,'seconds')

def execute_bubble_sort(lst):
    sorting_time = bubble_sort(lst, sorted(lst))
    print('List sorted in:',sorting_time,'seconds')

def execute_merge_sort(lst):
    sorting_time = merge_sort(lst, sorted(lst))
    print('List sorted in:',sorting_time,'seconds')

def execute_insertion_sort(lst):
    sorting_time = insertion_sort_gpt(lst, sorted(lst))
    print('List sorted in:',sorting_time,'seconds')

def main():
    os.system('cls')

    # Setting list length
    print('\033[1mType list length\033[0m')
    lst_lenght_str = input('Length: ')
    try:
        lst_lenght_int = int(lst_lenght_str)
        if lst_lenght_int <= 1:
            print('Length too small, shutting down...')
            exit(1)
    except ValueError:
        print('Invalid input, shuting down...')
        exit(1)
        
    lst = generate_list(lst_lenght_int)
    os.system('cls')

    # Choosing sorting algorithm
    print('Choose sorting algorithm\n1) Boggo\n2) Bubble\n3) Merge\n4) Insertion')
    algorithm = input('> ')
    if algorithm == '1':
        execute_boggo_sort(lst)
    elif algorithm == '2':
        execute_bubble_sort(lst)
    elif algorithm == '3':
        execute_merge_sort(lst)
    elif algorithm == '4':
        execute_insertion_sort(lst)
    else:
        print('Wrong inpurt, shuting down...')
        

if __name__ == "__main__":
    main()