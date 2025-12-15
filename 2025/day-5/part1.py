# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> tuple[list[tuple], list[int]]:
    intervals = []  # entries formated as (start, end)
    ingredients = []
    with open(path, 'r', encoding='utf-8') as f:
        are_ranges = True
        for line in f:
            line = line.strip()
            if line == "":
                are_ranges = False
                continue
            if are_ranges:
                start_and_end = line.split("-")
                intervals.append((int(start_and_end[0]), int(start_and_end[1])))
            else:
                ingredients.append(int(line))
    return intervals, ingredients

# # helper function to merge any overlapping intervals the given list (which have already been sorted by start time, ascending)
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    merged_intervals = [intervals[0]]
    for interval in intervals[1:]:
        prev_start, prev_end = merged_intervals[-1]
        cur_start, cur_end = interval
        if cur_start > prev_end:
            # no overlap in this case, so just append it
            merged_intervals.append(interval)
        else:
            merged_intervals[-1] = (prev_start, max(cur_end, prev_end))
    return merged_intervals

# helper function to perform binary search on given intervals 
def search_intervals(intervals, target: int) -> bool:
    l = 0
    r = len(intervals) - 1
    while l <= r:
        mid = l + (r-l) // 2
        start, end = intervals[mid]
        if target >= start and target <= end:
            return True
        # since we are sorting by start, filter based on the start value first
        if start < target:
            l = mid + 1
        else:
            r = mid - 1
    return False

def solution(intervals: list[tuple[int, int]], ingredients: list[int]) -> int:
    """
    Approach: merge intervals, then do binary search for each ingredient.
    This should take nlog(n) time total
    """

    # for now, see if we can get away with just sorting then doing binary search
    intervals = sorted(intervals, key=lambda x: x[0])
    intervals = merge_intervals(intervals)
    num_fresh = 0
    for ingredient in ingredients:
        if search_intervals(intervals, ingredient):
            num_fresh += 1
    return num_fresh

if __name__ == "__main__":
    input_path = "input.txt"
    intervals, ingredients = read_input(input_path)
    output = solution(intervals, ingredients)
    print("output = ", output)
