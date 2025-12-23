"""
Link: https://adventofcode.com/2025/day/2#part2
"""

from math import log10, pow

def read_input(path) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

# the main worker function, given a range, returns the sum of all inavlid IDs
# within that range
def get_invalid_ids(start: int, end: int) -> int:
    """
    Approach: get the prefix for this range (the first half of the start string)
    and generate all invalid IDs until we go above the end of the range.
    Repeat this for each chunk size
    """
    tot = 0
    print(f"Testing range {start}-{end}")
    invalid_ids = set()
    for times_repeated in range(2, len(str(start)) + 1):
        as_str = str(start)
        as_str = as_str[:len(as_str) // times_repeated]
        if as_str == '':
            as_str = '1'
        cur = int(as_str)
        while True:
            to_test = int(str(cur) * times_repeated)
            # skip cases where splitting the string in half on odd-length start 
            # results in considering a range before start
            if to_test < start:
                cur += 1
                continue
            if to_test <= end and to_test not in invalid_ids:
                print("invalid ID detected:", str(to_test))
                tot += to_test
                invalid_ids.add(to_test)
                cur += 1
            # just move on to the next one, don't break
            elif to_test in invalid_ids:
                cur += 1
            else:
                break
    print(f"Total for range {start}-{end}: {tot}")
    return tot

def solution(input_path):
    bounds = []
    input = read_input(input_path)
    for bound in input.split(','):
        start, end = bound.split('-')
        bounds.append((int(start), int(end)))
    tot = 0
    for s, e in bounds:
        print(f"given s,e: {s}-{e}")
        # split the range such that start and end have the same number of digits.
        # without this condition, handling the first digit over and over would be broken
        # ex: 99-112 would't check 111, since it would go from 99 -> 1010
        local_range = []
        while (int(log10(s)) < int(log10(e))):
            upper_bound = int(pow(10, int(log10(s))+1))
            local_range.append((s, upper_bound-1))
            s = upper_bound
        local_range.append((s,e))
        print("local_range:", local_range)
        for start, end in local_range:
            tot += get_invalid_ids(start,end)
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    output = solution(input_path)
    print(f"Soution: {output}")
