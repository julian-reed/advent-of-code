from copy import deepcopy
UPPER_LIMIT = 100
def read_input(path: str) -> list[tuple[int, int]]:
    machines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            machine_dir = {}
            all_contents = line.strip().split(' ')
            indicator_with_ints = ['0' if light == '.' else '1' for light in all_contents[0][1:-1]]
            machine_dir["indicator"] = "".join(indicator_with_ints)
            machine_dir["joltage"] = all_contents[-1][1:-1]
            buttons = []
            # describe buttons as strings so we can do xor
            for button in all_contents[1:-1]:
                button_list = ['0'] * len(machine_dir["indicator"])
                # remove parenthesis, and split on comma
                switches = button[1:-1].split(',')
                for switch in switches:
                    button_list[int(switch)] = '1'
                buttons.append("".join(button_list))
            machine_dir["buttons"] = buttons
            machines.append(machine_dir)
    return machines

# helper function to perform binary xor on two string inputs
def xor(s1, s2) -> str:
    n1 = int(s1, 2)
    n2 = int(s2, 2)
    res = n1 ^ n2
    # convert to binary, cut off "0b"
    bin_res = bin(res)[2:]
    # pad with correct number of bits
    return bin_res.zfill(len(s1))

def find_fewest_presses(cache, buttons, state, presses, seen) -> int:
    if presses >= UPPER_LIMIT:
        return presses
    if state in cache:
        print(f"State already in cache: {state}, value = {cache[state]}")
        return cache[state]
    min_val = UPPER_LIMIT
    for button in buttons:
        new_state = xor(state, button)
        # prune this branch if we have already seen this state, as this creates a cycle and can't be optimal
        print(f"xor of {state}, {button} = {new_state}. Seen = {seen}")
        if new_state in seen:
            print("Cycle detected, continuing")
            continue
        if new_state not in cache or cache[new_state] == UPPER_LIMIT:
            # print(f"State {new_state} not found in cache. Calculating...")
            # add new state to the cache
            cache[new_state] = find_fewest_presses(cache, buttons, deepcopy(new_state), presses + 1, deepcopy(seen | {new_state}))
        min_val = min(min_val, cache[new_state] + 1)
    cache[state] = min_val
    print(f"Adding state {state} to cache, value = {min_val}")
    return cache[state]

def solution(machines) -> int:
    # approach: try all possible positions, return the minimum from the current spot. BFS.
    # uses an UPPER LIMIT I defined since recursion could go on forever
    tot = 0
    for i, machine in enumerate(machines):
        init_state = "0" * len(machine["indicator"])
        print("init_state:", init_state)
        cache = {init_state:0}
        local_tot = find_fewest_presses(cache, machine["buttons"], machine["indicator"], 0, set())
        tot += local_tot
        print(f"total for machine {i}: {local_tot}")
        print("cache:", cache)
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
