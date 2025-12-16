from pprint import pprint
# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> tuple[list[list[str]], int]:
    grid = []
    with open(path, 'r', encoding='utf-8') as f:
        first_line = True
        for line in f:
            line = line.strip()
            if first_line:
                to_add = []
                for i, ch in enumerate(line):
                    to_add.append(ch)
                    if ch == 'S':
                        start_col = i
                grid.append(to_add)
                first_line = False
            else:
                grid.append(list(line))
    return grid, start_col


def solution(grid: list[list[str]], start_col: int) -> int:
    # include padding on the left and right sides
    table = [[0] * (len(grid[0])+2) for i in range(len(grid))]
    to_add = [0 if i in [0, len(grid[0])+1] else 1 for i in range(len(grid[0])+2)]
    table[-1] = to_add
    # print(table)
    # populate the table with appropriate values, bottom up
    for r in range(len(grid)-2, -1, -1):
        for c in range(len(grid[0])):
            # use c+1 to avoid padding in the list
            local = c+1
            table[r][local] = table[r+1][local] if grid[r+1][c] != '^' else (table[r+1][local-1] + table[r+1][local+1])

    # return get_total_timelines(0, start_col)
    # print("updated table")
    # pprint(table)
    return table[0][start_col+1]

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    grid, start_col = read_input(input_path)
    output = solution(grid, start_col)
    print("output = ", output)
