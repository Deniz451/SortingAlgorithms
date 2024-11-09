import time
import visualize_list

def bubble_sort(lst, target_lst):
    start_time = time.time()
    shuffle_count, iterration, x = 0, 0, 0

    while lst != target_lst:
        if lst[x] > lst[x+1]:
            lst[x], lst[x+1] = lst[x+1], lst[x]
        x += 1
        # adds 1 every time 2 elements swap for time calculation
        shuffle_count += 1 
        if x + 1 >= len(lst) - iterration:
            x = 0
            # adds 1 every time algorithm reaches end of the list
            iterration += 1

        time.sleep(0.05)
        visualize_list.visualize_list(lst)

    sorting_time = (time.time() - start_time) - shuffle_count * 0.05
    return sorting_time