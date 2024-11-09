import time
import visualize_list

shuffle_count = 0

def merge_sort(lst, target_lst):
    start_time = time.time()

    split_lst(lst)

    sorting_time = (time.time() - start_time) - shuffle_count * 0.05
    return sorting_time

def split_lst(lst):
    global shuffle_count

    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = split_lst(lst[:mid])
        right = split_lst(lst[mid:])

        visualize_list.visualize_list(lst)
        time.sleep(0.05)
        shuffle_count += 1

        return merge_lsts(left, right)
    
def merge_lsts(left, right):
    global shuffle_count
    result = []
    
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result.extend(left)
    result.extend(right)

    visualize_list.visualize_list(result)
    time.sleep(0.05)
    shuffle_count += 1
    
    return result
    