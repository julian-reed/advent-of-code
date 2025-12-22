from collections import deque
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

def find_fewest_presses(buttons, target) -> int:
    """
    Approach: use bfs
    """
    init_state = "0" * len(target)
    visited = set()
    locs = deque()
    locs.appendleft((init_state, 0))
    while locs:
        # pop to get the current state
        state, presses = locs.pop()
        print(f"Handling state {state}, with {presses}")
        if state == target:
            return presses
        if state in visited:
            print(f"State {state} found in visited")
            continue
        visited.add(state)
        for button in buttons:
            new_state = xor(state, button)
            print(f"xor({state}, {button}) = {new_state}")
            locs.appendleft((new_state, presses + 1))
    return float('inf')


def solution(machines) -> int:
    tot = 0
    for i, machine in enumerate(machines):
        local_tot = find_fewest_presses(machine["buttons"], machine["indicator"])
        tot += local_tot
        print(f"total for machine {i}: {local_tot}")
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
