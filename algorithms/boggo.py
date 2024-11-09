import random
import time
import visualize_list

def boggo_sort(lst, target_lst):
    start_time = time.time()
    shuffle_count = 0

    while lst != target_lst:
        lst = shuffle_list_rand(lst)
        shuffle_count += 1 
        time.sleep(0.05)
        visualize_list.visualize_list(lst)

    sorting_time = (time.time() - start_time) - shuffle_count * 0.05
    return sorting_time

def shuffle_list_rand(lst):
    for i in range(len(lst)):
        rand_index = random.randint(0, len(lst) - 1)
        lst[i], lst[rand_index] = lst[rand_index], lst[i]
    return lst