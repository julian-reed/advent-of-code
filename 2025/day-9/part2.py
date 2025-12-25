from collections import deque
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
def range_is_valid(invalid_tiles, t1, t2) -> bool:
    print(f"checking tiles {t1} and {t2}")
    min_r = min(t1[0], t2[0])
    max_r = max(t1[0], t2[0])
    min_c = min(t1[1], t2[1])
    max_c = max(t1[1], t2[1])
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            if (r,c) in invalid_tiles:
                return False
    return True

# helper function to fill in the boundary, updates the valid_tiles set via dfs
def fill_invalid(invalid_tiles, boundary, initial_r, initial_c) -> None:
    queue = deque()
    queue.append((initial_r, initial_c))
    while queue:
        r, c = queue.pop()
        # continue if we already saw this combo
        if (r,c) not in invalid_tiles and (r,c) not in boundary:
            invalid_tiles.add((r,c))
            queue.append((r+1,c))
            queue.append((r-1,c))
            queue.append((r,c+1))
            queue.append((r,c-1))

# helper function for optimization, checks if any invalid rectangles are inscribed
# in the rectangle from original tiles to new tile
def contains_invalid(invalid_tiles, original_tile, new_tile):
    l = min(original_tile[0], new_tile[0])
    r = max(original_tile[0], new_tile[0])
    bottom = min(original_tile[1], new_tile[1])
    top = max(original_tile[1], new_tile[1])
    for x, y in invalid_tiles:
        if (x >= l and x <= r) and (y >= bottom and y <= top):
            return True
    return False

def solution(tiles: list[tuple[int, int]]) -> int:
    """
    Approach: define the boundary, then flood fill the boundary to get all valid points, then check for possible solutions
    """
    boundary = set()
    max_r = tiles[0][0]
    min_r = tiles[0][0]
    min_c = tiles[0][1]
    max_c = tiles[0][1]
    for i in range(len(tiles)):
        cur = tiles[i]
        next = tiles[(i+1) % len(tiles)]
        for r in range(min(cur[0], next[0]), max(cur[0], next[0]) + 1):
            max_r = max(max_r, r)
            min_r = min(min_r, r)
            for c in range(min(cur[1], next[1]), max(cur[1], next[1]) + 1):
                boundary.add((r,c))
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    print("Boundary:", boundary)

    # it is actually a difficult problem to pick a point we know is inside the boundary (which we must do to start flood fill)
    # so my approach is this: track the min/max x and y of the boundary, and make a box which we know surronds the boundary with
    # two ticks of padding on each side.
    # then, flood fill this box to get all points OUTSIDE of the boundary
    # to check if a given rectangle is valid, see if it contains any of these invalid points
    bound_min_r = min_r - 2
    bound_max_r = max_r + 2
    bound_min_c = min_c - 2
    bound_max_c = max_c + 2
    bounding_box = set()
    for r in range(bound_min_r, bound_max_r + 1):
        bounding_box.add((r, bound_min_c))
        bounding_box.add((r, bound_max_c))
    for c in range(bound_min_c, bound_max_c + 1):
        bounding_box.add((bound_min_r, c))
        bounding_box.add((bound_max_r, c))


    print("Bounding box:", bounding_box)
    invalid_tiles = bounding_box
    fill_invalid(invalid_tiles, boundary, bound_min_r + 1, bound_min_c + 1)

    # iterate through all possible combos again, but check to ensure the range is valid as well
    max_area = -1
    for i in range(len(tiles)):
        # for optimization purposes: the current two tiles must be invald if the rectangle they make contains
        # one which is already invalid
        invalid_tiles = set()
        for j in range(i+1, len(tiles)):
            cur_area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
            if cur_area > max_area and not contains_invalid(invalid_tiles, tiles[i], tiles[j]):
                if range_is_valid(invalid_tiles, tiles[i], tiles[j]):
                    print(f"New max area: {cur_area} from points {tiles[i]} and {tiles[j]}")
                    max_area = cur_area
                else:
                    invalid_tiles.add(tiles[j])
    return max_area

if __name__ == "__main__":
    # input_path = "input.txt"
    input_path = "small_input.txt"
    tiles = read_input(input_path)
    output = solution(tiles)
    print("output = ", output)
