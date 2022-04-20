import random as rd
import time

length = 40000
list = list(range(1, length))
rd.shuffle(list)

def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        current = i
        previous = i - 1

        while current > 0 and array[previous] > current_value:
            array[current] = array[previous]
            current -= 1
            previous -= 1

        array[current] = current_value
    return array


start_time = time.time()
insertion_sort(list)
print("--- {} seconds --- for arr of length {}".format(time.time() - start_time, length))
