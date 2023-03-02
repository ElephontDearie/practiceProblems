from math import floor

def find_peak(input_array: list(), swap_operations: list(list())):
    for op in swap_operations:
        item_to_move = input_array.pop(op[1])
        new_index = op[0]
        input_array.insert(new_index, item_to_move)
    
    sorted_array = sorted(input_array)
    largest = get_largest_num(sorted_array)
    return input_array.index(largest)


def get_largest_num(sorted_array: list()):
    if len(sorted_array) == 1: 
        return sorted_array[0]

    midpoint = floor(len(sorted_array) / 2)
    largest = sorted_array[midpoint]

    if sorted_array[midpoint + 1] and sorted_array[midpoint + 1] > largest:
        largest = sorted_array[midpoint + 1]
        return get_largest_num(sorted_array[midpoint + 1:])
    elif sorted_array[midpoint - 1] and sorted_array[midpoint - 1] > largest:
        largest = sorted_array[midpoint - 1]
        return get_largest_num(sorted_array[:midpoint - 1])
