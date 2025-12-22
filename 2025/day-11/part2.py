from collections import deque
START = "svr"
REQUIRED = ["dac", "fft"]
def read_input(path: str) -> dict:
    adj = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            split_line = line.strip().split(" ")
            adj[split_line[0][:-1]] = split_line[1:] 
    return adj

# recurisve helper function, returns the number of paths possible from the starting point "cur"
def rec_sol(adj, cache, cur, req_status, state_map) -> None:
    tot = 0
    # alternatively, you could add "out" and its accompanying values directly to the cache
    # in the calling function to avoid this check each time
    if cur == "out":
        cache[(cur, req_status)] = 1 if req_status == ("1" * len(REQUIRED)) else 0
        return
    new_status = req_status
    if cur in REQUIRED:
        # this is an O(n) runtime, so it works here since n is small (2), but might kill runtime
        # with a larger set of required characters
        new_status = req_status[:state_map[cur]] + "1" + req_status[state_map[cur]+1:]
    for val in adj[cur]:
        if (val, new_status) not in cache:
            rec_sol(adj, cache, val, new_status, state_map)
        tot += cache[(val, new_status)]
    cache[(cur, req_status)] = tot

def solution(adj) -> int:
    cache = {}
    # store as a string so it is hashable, this string encodes a bit table
    req_status = "0" * len(REQUIRED)
    state_map = {state: idx for idx, state in enumerate(REQUIRED)}
    rec_sol(adj, cache, START, deepcopy(req_status), state_map)
    print(cache)
    return cache[(START, req_status)]

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
