"""
Note: like day 12, as far as I can tell this solution is correct. However, it is not fully optimized
and thus does not run in a reasonable amount of time for my full puzzle input. I imagine that a linear
programming approach could be used to solve within a reasonable time, but as I am unfamilar with that
technique, and I'm trying to do all of this without looking anything up, I am going to leave my solution
here.
"""
from collections import deque
def read_input(path: str) -> list[tuple[int, int]]:
    machines = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            machine_dir = {}
            all_contents = line.strip().split(' ')
            indicator_with_ints = ['0' if light == '.' else '1' for light in all_contents[0][1:-1]]
            machine_dir["indicator"] = "".join(indicator_with_ints)
            machine_dir["joltage"] = tuple([int(val) for val in all_contents[-1][1:-1].split(",")])
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

# helper function to apply the button press
def apply_button(state, button) -> list:
    return tuple([state[idx] + int(button[idx]) for idx in range(len(button))])

def find_fewest_presses(buttons, target) -> int:
    """
    Approach: use dfs
    """
    init_state = tuple([0] * len(target))
    print("init_state =", init_state)
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
            new_state = apply_button(state, button)
            # print(f"xor({state}, {button}) = {new_state}")
            locs.appendleft((new_state, presses + 1))
    return float('inf')


def solution(machines) -> int:
    tot = 0
    for i, machine in enumerate(machines):
        local_tot = find_fewest_presses(machine["buttons"], machine["joltage"])
        tot += local_tot
        print(f"total for machine {i}: {local_tot}")
    return tot

if __name__ == "__main__":
    # input_path = "input.txt"
    input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
