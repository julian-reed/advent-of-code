"""
Note: After doing some reading online, it seems like this problem can be solved with a reasonable runtime if you make certain assumptions
about the input. However, since I want my code to work in the general case (with the lower bound of the area of the polygon given), I will
leave my code in its current state: it should be correct, but doesn't make any simplifying assunptions. Thus, I won't be getting the star
for part 2, but I am left satisfied with my work nontheless :)
"""

from collections import deque
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
    min_x = min(t1[0], t2[0])
    max_x = max(t1[0], t2[0])
    min_y = min(t1[1], t2[1])
    max_y = max(t1[1], t2[1])
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # print(f"looking at point ({x}, {y}))")
            if (x,y) in invalid_tiles:
                return False
    return True

# helper function to fill in the boundary, updates the valid_tiles set via dfs
def fill_invalid(invalid_tiles, boundary, initial_x, initial_y) -> None:
    queue = deque()
    queue.append((initial_x, initial_y))
    while queue:
        x, y = queue.pop()
        # continue if we already saw this combo
        if (x,y) not in invalid_tiles and (x,y) not in boundary:
            invalid_tiles.add((x,y))
            queue.append((x+1,y))
            queue.append((x-1,y))
            queue.append((x,y+1))
            queue.append((x,y-1))

# helper function for optimization, checks if any invalid rectangles are inscribed
# in the rectangle from original tiles to new tile
def contains_invalid(invalid_tiles, original_tile, new_tile):
    l = min(original_tile[0], new_tile[0])
    r = max(original_tile[0], new_tile[0])
    bottom = min(original_tile[1], new_tile[1])
    top = max(original_tile[1], new_tile[1])
    for x, y in invalid_tiles:
        if (x >= l and x <= r) and (y >= bottom and y <= top):
            # print(f"invalid tile ({x}, {y}) inscibed by current tile {new_tile}")
            return True
    return False

def solution(tiles: list[tuple[int, int]]) -> int:
    """
    Approach: define the boundary, then flood fill the boundary to get all valid points, then check for possible solutions
    """
    boundary = set()
    max_x = tiles[0][0]
    min_x = tiles[0][0]
    min_y = tiles[0][1]
    max_y = tiles[0][1]
    for i in range(len(tiles)):
        cur = tiles[i]
        next = tiles[(i+1) % len(tiles)]
        for x in range(min(cur[0], next[0]), max(cur[0], next[0]) + 1):
            max_x = max(max_x, x)
            min_x = min(min_x, x)
            for y in range(min(cur[1], next[1]), max(cur[1], next[1]) + 1):
                boundary.add((x,y))
                min_y = min(min_y, y)
                max_y = max(max_y, y)
    print("Boundary:", boundary)

    # it is actually a difficult problem to pick a point we know is inside the boundary (which we must do to start flood fill)
    # so my approach is this: track the min/max x and y of the boundary, and make a box which we know surronds the boundary with
    # two ticks of padding on each side.
    # then, flood fill this box to get all points OUTSIDE of the boundary
    # to check if a given rectangle is valid, see if it contains any of these invalid points
    bound_min_x = min_x - 2
    bound_max_x = max_x + 2
    bound_min_y = min_y - 2
    bound_max_y = max_y + 2
    # print(f"bounding box boundaries: min_x = {bound_min_x}, max_x = {bound_max_x}, min_y = {bound_min_y}, max_y = {bound_max_y}")
    bounding_box = set()
    for x in range(bound_min_x, bound_max_x + 1):
        bounding_box.add((x, bound_min_y))
        bounding_box.add((x, bound_max_y))
    for y in range(bound_min_y, bound_max_y + 1):
        bounding_box.add((bound_min_x, y))
        bounding_box.add((bound_max_x, y))


    invalid_tiles = bounding_box
    fill_invalid(invalid_tiles, boundary, bound_min_x + 1, bound_min_y + 1)
    print("invalid_tiles:", sorted(invalid_tiles))
    # iterate through all possible combos again, but check to ensure the range is valid as well
    max_area = -1
    for i in range(len(tiles)):
        # for optimization purposes: the current two tiles must be invald if the rectangle they make contains
        # one which is already invalid
        invalid_locs = set()
        # print("reseting invalid locs")
        for j in range(i+1, len(tiles)):
            cur_area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
            if cur_area > max_area and not contains_invalid(invalid_locs, tiles[i], tiles[j]):
                if range_is_valid(invalid_tiles, tiles[i], tiles[j]):
                    print(f"New max area: {cur_area} from points {tiles[i]} and {tiles[j]}")
                    max_area = cur_area
                else:
                    invalid_locs.add(tiles[j])
                    print(f"adding {tiles[j]} to invalid_locs")
    return max_area

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    tiles = read_input(input_path)
    output = solution(tiles)
    print("output = ", output)
