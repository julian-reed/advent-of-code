# helper function to parse given text file into a 2-D array
def read_input(path: str) -> list[list[str]]:
    arr = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            arr.append(list(line.strip()))
    return arr

def solution(arr: list[list[str]]) -> int:
    # this approach will recalculate all surrounding values each time.
    # you could use a sliding window to save some of those calls, but
    # since it is asymptotically the same, I'll skip this for readability
    total_removed = 0
    recently_removed = 1
    while recently_removed > 0:
        recently_removed = 0
        for r in range(len(arr)):
            for c in range(len(arr[0])):
                adj = 0
                valid_cols = [c-1, c, c+1]
                valid_rows = [r-1, r, r+1]
                if r+1 >= len(arr):
                    valid_rows = valid_rows[:2]
                if r-1 < 0:
                    valid_rows = valid_rows[1:]
                if c+1 >= len(arr[0]):
                    valid_cols = valid_cols[:2]
                if c-1 < 0:
                    valid_cols = valid_cols[1:]
                for vc in valid_cols:
                    for vr in valid_rows:
                        if arr[vr][vc] == '@' and not (vr == r and vc == c):
                            adj += 1
                if adj < 4 and arr[r][c] == '@':
                    recently_removed += 1
                    # change it immediately
                    arr[r][c] = 'X'
        total_removed += recently_removed

    return total_removed

if __name__ == "__main__":
    input_path = "input.txt"
    paper_map = read_input(input_path)
    output = solution(paper_map)
    print("output = ", output)
