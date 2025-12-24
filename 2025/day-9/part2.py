from pprint import pprint
# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> list[tuple[int, int]]:
    tiles = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            tile_points = [int(pt) for pt in line.strip().split(',')]
            tiles.append(tuple(tile_points))
    return tiles

# helper function to determine if all tiles between t1 and t2 are green/red
def range_is_valid(max_y_by_x, t1, t2) -> bool:
    print(f"checking tiles {t1} and {t2}")
    max_y = max(t1[1], t2[1])
    min_y = min(t1[1], t2[1])
    r = max(t1[0], t2[0])
    l = min(t1[0], t2[0])
    for x in range(l, r + 1):
        if x not in max_y_by_x:
            return False
        max_at_x, min_at_x = max_y_by_x[x]
        if max_y > max_at_x or min_y < min_at_x:
            # print(f"invalid")
            return False
    # print(f"valid")
    return True

# helper function to connect t1 to t2, and update the dict accordingly
def connect_tiles(max_y_by_x, t1, t2) -> None:
    # connect with same x val
    if t1[0] == t2[0]:
        x = t1[0]
        larger_y = max(t1[1], t2[1])
        smaller_y = min(t1[1], t2[1])
        existing_val = max_y_by_x.get(x, None)
        if existing_val is None:
            max_y_by_x[x] = (larger_y, smaller_y)
        else:
            max_y_by_x[x] = ((max(existing_val[0], larger_y), min(existing_val[1], smaller_y)))
    # they must have the same y val
    else:
        smaller_x = min(t1[0], t2[0])
        larger_x = max(t1[0], t2[0])
        y = t1[1]
        for x in range(smaller_x, larger_x + 1):
            existing_val = max_y_by_x.get(x)
            if existing_val is None:
                max_y_by_x[x] = (y, y)
            else:
                max_y_by_x[x] = (max(existing_val[0], y), min(existing_val[1], y))

def solution(tiles: list[tuple[int, int]]) -> int:
    """
    Approach: iterate through the entire list of tiles to find the range of y values that are green, for each x.
    """
    print("tiles", tiles)
    max_y_by_x = {} # maps x value to (largest y value, smallest y value) which contains all green tiles
    # populate max_y_by_x
    for i in range(len(tiles)):
        connect_tiles(max_y_by_x, tiles[i], tiles[(i+1) % len(tiles)])
    print("max_y_by_x:")
    pprint(max_y_by_x)
    # iterate through all possible combos again, but check to ensure the range is valid as well
    max_area = -1
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            # optimization: track which ranges are invalid, and any shape which conatins an invalid one inscribed
            # must also be invalid
            cur_area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
            if cur_area > max_area and range_is_valid(max_y_by_x, tiles[i], tiles[j]):
                print(f"New max area: {cur_area} from points {tiles[i]} and {tiles[j]}")
                max_area = cur_area
    return max_area

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    tiles = read_input(input_path)
    output = solution(tiles)
    print("output = ", output)
