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

def find_fewest_presses(machine) -> int:
    # approach:
    return 0

def solution(machines) -> int:
    return sum(find_fewest_presses(machine) for machine in machines)

if __name__ == "__main__":
    # input_path = "input.txt"
    input_path = "small_input.txt"
    machines = read_input(input_path)
    output = solution(machines)
    print("output = ", output)
