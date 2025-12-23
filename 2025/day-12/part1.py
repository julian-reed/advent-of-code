"""
Note: this solution is too slow, even for the example input on part 1. I'm sure this approach can be optimized a
bit, but I suspect some sort of linear programming solution is required, which I currently do not know how to do
without looking online. Therefore, I'm ending here, with code that should be right (although I can't fully test it),
but is inefficient. Looking forward to next year!
"""

from copy import deepcopy
from collections import deque
# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> tuple:
    shapes = []
    # formated as ((width, length), present_quantities)
    regions = []
    with open(path, 'r', encoding='utf-8') as f:
        are_shapes = True
        shape = []
        for line in f:
            line = line.strip()
            if are_shapes and 'x' in line:
                are_shapes = False
            if are_shapes:
                if line == "":
                    shapes.append(shape)
                    continue
                if ':' in line:
                    shape = []
                    continue
                shape.append([0 if ch == '.' else 1 for ch in line])
            else:
                l, r = line.split(":")
                width, length = l.split("x")
                # ignore empty space which will be the first element after splitting
                quantities = [int(val) for val in r.split(" ")[1:]]
                regions.append({"width":int(width), "length":int(length), "quantities":tuple(quantities)})
    return shapes, regions

# helper function which finds all possible locations for the current shape,
# and returns a list of grid states after adding the shape in each respective location
def find_and_add(grid, orientations) -> list:
    grids = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            for cur_shape in orientations:
                test = deepcopy(grid)
                broken = False
                for sr in range(len(cur_shape)):
                    if broken:
                        break
                    for sc in range(len(cur_shape[0])):
                        if cur_shape[sr][sc] == 1:
                            if r+sr >= len(test) or c+sc >= len(test[0]) or test[r + sr][c + sc] == 1:
                                broken = True
                                del test
                                break
                            else:
                                test[r+sr][c+sc] = 1
                if broken:
                    continue
                # if merging the current shape was never broken, then we have a valid location
                grids.append(test)
    return grids

# helper function to see if this region can be satisfied
def can_presents_fit(shapes, orientations, region) -> bool:
    queue = deque()
    grid = [[0] * region["width"] for i in range(region["length"])]
    queue.append((grid, region["quantities"]))
    while queue:
        g, quantities = queue.pop()
        print(f"Handling graph {g}. Quantities = {quantities}")
        if quantities == tuple([0] * len(quantities)):
            return True
        # only try the next shape up. If we can't find a way to place that shape,
        # then no solution is valid
        next_shape = -1
        for idx in range(len(quantities)):
            if quantities[idx] > 0:
                next_shape = idx
                # subtract one to indicate that we are placing this shape
                quantities = quantities[:idx] + (quantities[idx]-1,) + quantities[idx+1:]
                break
        updated_grids = find_and_add(g, orientations[next_shape])
        for ug in updated_grids:
            queue.append((ug, quantities))

    return False

# helper function to get each possible orientation for each shape
def get_orientations(shapes) -> list:
    orientations = []
    for shape in shapes:
        orientations_for_shape = []
        # strategy: rotate, and also add a version of that rotation flipped across y axis
        # rotate 90 degrees
        # left col = bottom row, mid col = mid row, right col = top row
        r1 = []
        for c in range(len(shape[0])-1, -1, -1):
            col = []
            for r in range(len(shape)):
                col.append(shape[r][c])
            r1.append(col)

        # rotate 180 degrees
        # to do this, switch left and rightmost columns from original shape, and flip across x axis
        r2 = deepcopy(shape)
        for r in range(len(shape)):
            r2[r][0], r2[r][-1] = r2[r][-1], r2[r][0]
        r2[0], r2[-1] = r2[-1], r2[0]

        # rotate 270 degrees
        # to do this, switch top and bottom rows of r1, and flip all rows across y axis
        r3 = [l[::-1] for l in r1]
        r3[0], r3[-1] = r3[-1], r3[0]
        

        for s in [shape, r1, r2, r3]:
            # after rotating, flip across x axis
            flipped = [l[::-1] for l in s]
            # add them to local orientations if they aren't duplicates (O(1) operation)
            if s not in orientations_for_shape:
                orientations_for_shape.append(s)
            if flipped not in orientations_for_shape:
                orientations_for_shape.append(flipped)

        orientations.append(orientations_for_shape)
    return orientations

def solution(shapes, regions) -> int:
    """
    Approach: since we just care about if there exists a way to fit
    all of the presents, use dfs
    """
    orientations = get_orientations(shapes)
    print("orientations:", orientations)
    count = 0
    for i, region in enumerate(regions):
        print("Starting region", i)
        if can_presents_fit(shapes, orientations, region):
            print("Presents fit in region", i)
            count += 1
        else:
            print("FAILURE: presents don't fit for region", i)
    return count

if __name__ == "__main__":
    # input_path = "input.txt"
    input_path = "small_input.txt"
    shapes, regions = read_input(input_path)
    output = solution(shapes, regions)
    print("output = ", output)
