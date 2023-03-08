from math import floor

def find_peak(input_array: list(), swap_operations: list(list())):
    peak_index = get_largest_num_index(input_array)

    for op in swap_operations:
        peak_in_swaps = peak_index in op
        if (peak_in_swaps):
            if (op[0] == peak_index):
                peak_index = op[1]
            elif (op[1] == peak_index):
                peak_index = op[0]

    return peak_index


def get_largest_num_index(array: list(), index_increment: int = 0):
    if len(array) == 1: 
        return index_increment
    if (len(array) == 2):
        return index_increment if array[0] > array[1] else index_increment + 1
    
    midpoint = floor(len(array) / 2) + index_increment
    largest = array[midpoint]
    largest_num_index = midpoint

    if array[midpoint + 1] and array[midpoint + 1] > largest:
        return get_largest_num_index(array[midpoint + 1:], midpoint + 1)
    elif array[midpoint - 1] and array[midpoint - 1] > largest:
        return get_largest_num_index(array[:midpoint - 1])
    return largest_num_index