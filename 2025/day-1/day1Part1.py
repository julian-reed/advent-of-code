"""
Day 1 Solution.
Link: https://adventofcode.com/2025/day/1
"""
DIAL_SIZE = 100

def read_input() -> str:
    with open("day1Input.txt", 'r', encoding='utf-8') as f:
        contents = f.read()
        return contents

# returns the solution for today's puzzle, which is how many times the dial
# is left pointing at 0 after any rotation
def solution() -> int:
    zero_count = 0
    pos = 50
    input = read_input()
    turns = input.split("\n")
    for turn in turns:
        if turn == '':
            continue
        dir = turn[0]
        dist = int(turn[1:]) % DIAL_SIZE
        if dir == 'R':
            pos = (pos + dist) % 100
        else:
            pos = 100 - dist + pos if dist > pos else pos - dist
        zero_count = zero_count + 1 if pos == 0 else zero_count
    return zero_count

if __name__ == "__main__":
    output = solution()
    print("Final answer:", output)

