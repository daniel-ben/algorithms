import random as rd
import time

length = 200000
list = list(range(1, length))
rd.shuffle(list)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    half = len(arr) // 2

    left_list = arr[:half]
    right_list = arr[half:]

    merge_sort(left_list)
    merge_sort(right_list)

    i = j = k = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            arr[k] = left_list[i]
            k += 1
            i += 1
        else:
            arr[k] = right_list[j]
            k += 1
            j += 1
        
    while i < len(left_list):
        arr[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        arr[k] = right_list[j]
        j += 1
        k += 1

    return list

start_time = time.time()
merge_sort(list)
print("--- {} seconds --- for arr of length {}".format(time.time() - start_time, length))