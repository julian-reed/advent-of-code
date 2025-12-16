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
    # recursive helper to find # of total timelines from a given row and column
    def get_total_timelines(r: int, c: int) -> int:
        # make sure we are in bounds
        if c >= len(grid[0]) or c < 0:
            return 0
        if r + 1 >= len(grid):
            return 1
        if grid[r+1][c] != '^':
            return get_total_timelines(r+1, c)
        else:
            return get_total_timelines(r+1, c-1) + get_total_timelines(r+1, c+1)


    return get_total_timelines(0, start_col)

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    grid, start_col = read_input(input_path)
    output = solution(grid, start_col)
    print("output = ", output)
