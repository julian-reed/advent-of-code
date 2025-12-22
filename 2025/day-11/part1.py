from collections import deque
from copy import deepcopy
def read_input(path: str) -> dict:
    adj = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            split_line = line.strip().split(" ")
            adj[split_line[0][:-1]] = split_line[1:] 
    return adj


def solution(adj) -> int:
    """
    approach: dfs
    assuming no cycles, not sure if this is a safe assumption
    """
    count = 0
    queue = deque()
    for val in adj["svr"]:
        queue.append((val, {"fft", "dac"}))
    while queue:
        cur, s = queue.pop()
        print(f"cur = {cur}, s = {s}")
        if cur == "out":
            if not s:
                count += 1
            continue
        if cur in s:
            s.remove(cur)
        for val in adj[cur]:
            queue.appendleft((val, deepcopy(s)))
    return count

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
