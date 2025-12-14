WINDOW_SIZE = 12

def read_input() -> str:
    with open("input.txt", 'r', encoding='utf-8') as f:
    # with open("custom_input.txt", 'r', encoding='utf-8') as f:
        return f.read().strip()

def solution() -> int:
    # get a list of batteries from the input
    batteries = read_input().split('\n')
    tot = 0
    for i, battery in enumerate(batteries):
    # for battery in batteries:
        """
        Approach: start with the first WINDOW_SIZE characters from the left.
        As you parse characters from the right, move them left while the character from the
        right is larger than the character directly to its left, and there are more characters
        remaining to the right to complete the full window.
        """
        digits = battery[:WINDOW_SIZE]
        # tracks which index we will try to merge next
        r = 1
        starting_l = 0
        while r < len(battery):
            # l is the index we are comparing battery[r] against
            starting_l = min(starting_l, WINDOW_SIZE - 1)
            l = starting_l
            print(f"l = {l}. digits[l] = {digits[l]}")
            # replace if the new digit is larger or equal to the existing digit, and
            # there is enough space afterwards
            while len(battery) - r >= (WINDOW_SIZE - l) and l >= 0 and digits[l] <= battery[r]:
                if digits[l] == battery[r]:
                    # check the next characters, only replace if the next characters are larger
                    chars_to_check_count = min(len(battery) - r - 1, WINDOW_SIZE - l - 1)
                    if chars_to_check_count == 0 or int(battery[r+1: r+1+chars_to_check_count]) < int(battery[r: r+chars_to_check_count]):
                        break
                l -= 1
            # see how many digits should be replaced, and replace them
            digits_to_replace = starting_l - l
            digits = digits[:l+1] + battery[r : r + digits_to_replace]
            # add additional length as necessary
            digits += battery[r+digits_to_replace : r + digits_to_replace + (WINDOW_SIZE - len(digits))]
            print(f"digits after replacement: {digits}, number of characters = {len(digits)}. Battery = {battery}")
            r += 1
            starting_l = l + 1
            if r < len(battery):
                print(f"New r value: {r}. battery[r] == {battery[r]}")
        print(f"max from battery {i}: {digits}. Original value: {battery}")
        tot += int(digits)
    return tot

if __name__ == "__main__":
    output = solution()
    print("Final answer:", output)

