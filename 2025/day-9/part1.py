# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> list[tuple[int, int]]:
    tiles = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            tile_points = [int(pt) for pt in line.strip().split(',')]
            tiles.append(tuple(tile_points))
    return tiles


def solution(tiles: list[tuple[int, int]]) -> int:
    """
    Approach: brute force by checking each point, this can probably be optimized
    """
    max_area = -1
    for i in range(len(tiles)):
        for j in range(i+1, len(tiles)):
            cur_area = (abs(tiles[i][0] - tiles[j][0]) + 1) * (abs(tiles[i][1] - tiles[j][1]) + 1)
            if cur_area > max_area:
                print(f"New max area: {cur_area} from points {tiles[i]} and {tiles[j]}")
                max_area = cur_area
    return max_area

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    tiles = read_input(input_path)
    output = solution(tiles)
    print("output = ", output)
