from typing import Any
from collections import defaultdict
# helper function to parse the input into interval and ingredient lists
def read_input(path: str):
    columns = defaultdict(list)
    # the current column ranges from col_starts[idx] to col_starts[idx]-2
    column_starts = []
    with open(path, 'r', encoding='utf-8') as f:
        # NOTE: unlike part 1, we don't want to convert each value to an int
        # therefore, remove this processing
        for line in f:
            for col, ch in enumerate(line):
                if ch == '\n':
                    break
                columns[col].append(ch)
                if ch in ['+', '*']:
                    column_starts.append(col)
    return columns, column_starts

def solution(columns, col_starts) -> int:
    tot = 0
    for i in range(len(col_starts)):
        s = col_starts[i]
        # ending index of column (not inclusive)
        e = col_starts[i+1] - 1 if i+1 < len(col_starts) else len(columns)
        should_add = columns[s][-1] == '+'
        local_tot = 0
        for c in range(s, e):
            cur = ""
            for r in range(len(columns[s])-1):
                if columns[c][r] != " ":
                    cur += columns[c][r]
            if c == s:
                local_tot = int(cur)
            else:
                local_tot = local_tot + int(cur) if should_add else local_tot * int(cur)
        tot += local_tot
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    cols, col_starts = read_input(input_path)
    output = solution(cols, col_starts)
    print("output = ", output)
