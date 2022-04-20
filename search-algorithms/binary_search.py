def binary_search(array, target):
    min = 0
    max = len(array) - 1

    while min <= max:
        mid = (min + max) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            min = mid + 1
        else:
            max = mid - 1
    
    return -1


def recursive_binary_search(array, min, max, target):
    if min > max:
        return -1

    mid = (min + max) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return recursive_binary_search(array, min, mid - 1, target)
    else:
        return recursive_binary_search(array, mid + 1, max, target)
