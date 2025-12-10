"""
Day 1, Part 2 Solution.
Link: https://adventofcode.com/2025/day/1#part2
"""

DIAL_SIZE = 100

def read_input() -> str:
    with open("day1Input.txt", 'r', encoding='utf-8') as f:
    # with open("test_input.txt", 'r', encoding='utf-8') as f:
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
        # dist = int(turn[1:])
        zero_count += int(turn[1:]) // DIAL_SIZE
        dist = int(turn[1:]) % DIAL_SIZE
        # if dir == 'R':
        #     pos += dist
        #     if pos >= 100:
        #         zero_count += 1
        #         pos %= 100
        if dir == "R":
            pos += dist
            zero_count += pos // 100
            pos %= 100
        else:
            zero_count = zero_count + 1 if pos - dist <= 0 and pos != 0 else zero_count
            pos = 100 - dist + pos if dist > pos else pos - dist
        print(f"just performed {turn}, current position = {pos}. zero_count = {zero_count}")
    return zero_count

if __name__ == "__main__":
    output = solution()
    print("Final answer:", output)

