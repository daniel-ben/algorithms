import random as rd
import time

length = 40000
list = list(range(1, length))
rd.shuffle(list)

def selection_sort(array):
	new_array = []

	for i in range(len(array)):
		min_index, min_number = find_min_value(array)
		new_array.append(min_number)
		array.pop(min_index)

	return new_array

def find_min_value(array):
	min_value  = array[0]
	min_key = 0

	for index in range(1, len(array)):
		if array[index] < min_value:
			min_value = array[index]
			min_key = index
	
	return min_key, min_value


start_time = time.time()
selection_sort(list)
print("--- {} seconds --- for arr of length {}".format(time.time() - start_time, length))
