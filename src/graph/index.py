

MAX_CHAR_IDX = 4
MAX_LINE_IDX = 4
def find_puddle(input):
    count = 0
    seen = []

    for i, line in enumerate(input):
        print(line)
        for j, char in enumerate(line):
            print(char)
            if char == "." and is_new(i, j, input):
                count += 1
                print(count)
    return count

def is_new(line_idx, char_idx, grid) -> bool:
    if char_idx < MAX_CHAR_IDX and is_puddle(grid[line_idx][char_idx + 1]): # right
        return True
    if line_idx < MAX_LINE_IDX and is_puddle(grid[line_idx + 1][char_idx]): # bottom
        return True

    if is_puddle(grid[line_idx][char_idx - 1]): # left
        return False
    if is_puddle(grid[line_idx - 1][char_idx]): # top
        return False

def is_puddle(char) -> bool:
    return char == "."