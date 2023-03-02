
def find_peak(input_array: list(), swap_operations: list(list())):
    for op in swap_operations:
        item_to_move = input_array.pop(op[1])
        new_index = op[0]
        input_array.insert(new_index, item_to_move)

    largest = input_array[0]
    for i in range(1, len(input_array) - 1):
        if (input_array[i] > largest):
            largest = i

    return largest