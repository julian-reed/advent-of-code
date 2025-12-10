"""
Day 1 Solution.
Link: https://adventofcode.com/2025/day/1
"""
from pathlib import Path

def read_input() -> str:
    with open("day1Input.txt", 'r', encoding='utf-8') as f:
        contents = f.read()
        return contents

# returns the solution for today's puzzle, which is how many times the dial
# is left pointing at 0 after any rotation
def solution() -> int:

if __name__ == "__main__":
    output = solution()
    print("Final answer:", output)

