import decimal

decimal.getcontext().prec = 6

initial_increment = 1

def get_square_root(num: int, middle: float = None, last_increment = 1, last_try = None):
    if (not middle):
        middle = num / 2
        print(middle)
    
    middle_calc = middle * middle
    if (middle_calc == num):
        return middle
    
    #  if middle_calc < num && last_try > num: last_increment / 2
    elif (middle_calc < num):
        return get_square_root(num, middle + 1)
    
    #  if middle_calc > num && last_try < num: last_increment * 2
    elif (middle_calc > num):
        return get_square_root(num, middle - 1)



