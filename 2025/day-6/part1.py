from typing import Any
# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> tuple[list[tuple], list[int]]:
    grid = []
    with open(path, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for line in f)
        # reset file pointer
        f.seek(0)
        line_counter = 0
        for line in f:
            list_to_add = [elem for elem in line.strip().split(' ') if elem != '']
            print(list_to_add)
            if line_counter < total_lines - 1:
                list_to_add = [int(elem) for elem in list_to_add]
            grid.append(list_to_add)
            line_counter += 1
    return grid

def solution(grid: list[list[Any]]) -> int:
    """
    Approach: iterate over each column of the grid and perform necessary operations
    """
    tot = 0
    for c in range(len(grid[0])):
        # there is nothing to perform if the grid only has operations,
        # maybe you should return a 0 in this case also?
        if len(grid) <= 1:
            break
        # we know the last entry is the operation to perform
        local_tot = grid[0][c]
        should_add = grid[-1][c] == '+'
        # don't include the last row since it is the operation, start with second row since the first is the
        # value of local_tot
        for r in range(1, len(grid) - 1):
            cur_val = grid[r][c]
            local_tot = local_tot + cur_val if should_add else local_tot * cur_val
        tot += local_tot
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    grid = read_input(input_path)
    output = solution(grid)
    print("output = ", output)
