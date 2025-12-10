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
    Approach: get the prefix for this range
    """
    tot = 0

    return tot

def solution(input_path):
    bounds = []
    input = read_input(input_path)
    for bound in input.split(','):
        start, end = bound.split('-')
        bounds.append((start, end))
    tot = 0
    for s, e in bounds:
        tot += get_invalid_ids(s,e)
    return tot

if __name__ == "__main__":
    input_path = "day2Input.txt"
    output = solution(input_path)
    print(f"Soution: {output}")
