from collections import deque
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
    for val in adj["you"]:
        queue.append(val)
    while queue:
        cur = queue.pop()
        if cur == "out":
            count += 1
            continue
        for val in adj[cur]:
            queue.append(val)
    return count

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
