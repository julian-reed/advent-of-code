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
    split_counter = 0
    beam_cols = set()
    beam_cols.add(start_col)
    # ignore last row since there won't be any splits there
    for r in range(len(grid) - 1):
        updated_cols = set()
        for c in beam_cols:
            if c >= len(grid[0]) or c < 0:
                continue
            if grid[r+1][c] == '^':
                split_counter += 1
                updated_cols.add(c-1)
                updated_cols.add(c+1)
            else:
                updated_cols.add(c)
        beam_cols = updated_cols
    return split_counter

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    grid, start_col = read_input(input_path)
    output = solution(grid, start_col)
    print("output = ", output)
