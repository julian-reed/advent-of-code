def read_input() -> str:
    # with open("test_input.txt", 'r', encoding='utf-8') as f:
    with open("input.txt", 'r', encoding='utf-8') as f:
        return f.read().strip()

def solution() -> int:
    # get a list of batteries from the input
    batteries = read_input().split('\n')
    tot = 0
    # for i, battery in enumerate(batteries):
    for battery in batteries:
        curMax = -1
        r = len(battery) - 1
        for l in range(len(battery)-2, -1, -1):
            if int(battery[l] + battery[r]) > curMax:
                curMax = int(battery[l] + battery[r])
                if int(battery[l]) > int(battery[r]):
                    r = l
        # print(f"max from battery {i}: {curMax}")
        tot += curMax
    return tot

if __name__ == "__main__":
    output = solution()
    print("Final answer:", output)

