import random as rd
import time

length = 200000
list = list(range(1, length))
rd.shuffle(list)

def quick_sort(array):
    if len(array) < 2:
        return array
    
    pivot = array[0]
    smaller_nums = [num for num in array[1:] if num <= pivot]
    greater_nums = [num for num in array[1:] if num > pivot]

    return quick_sort(smaller_nums) + [pivot] + quick_sort(greater_nums)


start_time = time.time()
quick_sort(list)
print("--- {} seconds --- for arr of length {}".format(time.time() - start_time, length))