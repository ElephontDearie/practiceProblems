import decimal
from enum import Enum

decimal.getcontext().prec = 7

initial_increment = 1

Size = Enum('Size', ['BIG', 'SMALL'])
default_increment = 0.000001

def get_square_root(target: int, range: list):
    middle = round(((range[0] + range[1]) / 2), 6)
    middle_calc = middle * middle

    if (middle_calc == target):
        return round(middle, 6)
    elif (range == [middle, range[1]] or range == [range[0], middle]):
        return round(middle, 6)
    
    elif (middle_calc < target):
        return get_square_root(target, [middle, range[1]])

    elif (middle_calc > target):
        return get_square_root(target, [range[0], middle])

