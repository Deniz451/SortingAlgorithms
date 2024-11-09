import time
import visualize_list

def insertion_sort(lst, target_lst):
    time_start = time.time
    index = 1

    while lst != target_lst:
        visualize_list.visualize_list(lst)
        time.sleep(0.05)

        for i in range(len(lst)):
            for j in range(i):
                if lst[i] < lst[j]:
                    
                    index += 1


    sorting_time = time_start - time.time - 0.05 * index
    return sorting_time

def insertion_sort_gpt(lst, target_list):
    start_time = time.time()
    index = 1  # Start at index 1 because the first element is already considered sorted

    while index < len(lst):  # Continue until all elements are sorted
        current_value = lst[index]  # The element to insert
        position = index

        # Shift elements of lst[0..index-1] that are greater than current_value to the right
        while position > 0 and lst[position - 1] > current_value:
            lst[position] = lst[position - 1]  # Shift the element to the right
            position -= 1  # Move left to the next position

        # Place the current_value at the correct position
        lst[position] = current_value
        index += 1  # Move to the next element
        
        visualize_list.visualize_list(lst)
        time.sleep(0.05)

    sorting_time = (time.time() - start_time) - index * 0.05  # Calculate sorting time
    return sorting_time