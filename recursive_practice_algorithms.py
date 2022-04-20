################## Recursive count items in array #####################

def recursive_count_items(array):
    if array == []:
        return 0
    return 1 + recursive_count_items(array[1:])

################## Recursive sum numbers #####################

def recursive_sum(array):
    if array == []:
        return 0
    return array[0] + recursive_sum(array[1:])

################## Find smallest number #####################

def recursive_find_min_value(array):
    if len(array) == 2:
        return array[0] if array[0] < array[1] else array[1]
    
    min_num = recursive_find_min_value(array[1:])
    return array[0] if array[0] < min_num else min_num

################## Find biggest number #####################

def recursive_find_max_value(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    
    max_num = recursive_find_max_value(array[1:])
    return array[0] if array[0] > max_num else max_num
