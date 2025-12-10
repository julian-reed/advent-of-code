"""
Link: https://adventofcode.com/2025/day/2
"""

def read_input(path) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

# the main worker function, given a range, returns the sum of all inavlid IDs
# within that range
def get_invalid_ids(start: int, end: int) -> int:
    """
    Approach: get the prefix for this range (the first half of the start string)
    and generate all invalid IDs until we go above the end of the range
    """
    tot = 0
    as_str = str(start)
    as_str = as_str[:len(as_str) // 2]
    if as_str == '':
        as_str = '1'
    cur = int(as_str)
    while True:
        to_test = int(str(cur) + str(cur))
        # skip cases where splitting the string in half on odd-length start 
        # results in considering a range before start
        if to_test < start:
            cur += 1
            continue
        if to_test <= end:
            tot += to_test
            cur += 1
        else:
            break
    return tot

def solution(input_path):
    bounds = []
    input = read_input(input_path)
    for bound in input.split(','):
        start, end = bound.split('-')
        bounds.append((int(start), int(end)))
    tot = 0
    for s, e in bounds:
        tot += get_invalid_ids(s,e)
    return tot

if __name__ == "__main__":
    input_path = "day2Input.txt"
    output = solution(input_path)
    print(f"Soution: {output}")
