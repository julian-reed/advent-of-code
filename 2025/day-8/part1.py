import math
PAIRS_TO_CONSIDER = 1000
NUM_LARGEST = 3
# helper function to parse the input into interval and ingredient lists
def read_input(path: str) -> tuple[list[tuple], list[int]]:
    boxes = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            to_add = [int(coord) for coord in line.strip().split(',')]
            boxes.append(tuple(to_add))
    return boxes

# helper function to find the distance between two points
def distance_between(box1: tuple[int, int, int], box2: tuple[int, int, int]):
    tot = 0
    for i in range(len(box1)):
        tot += math.pow((box2[i] - box1[i]), 2)
    return math.sqrt(tot)

def solution(boxes: list[tuple[int, int, int]]) -> int:
    box_pairs = []
    box_to_circuit = {}
    circuit_to_boxes = {}   # maps from circuit # to # of boxes in that circuit
    for i in range(len(boxes)):
        box_to_circuit[boxes[i]] = i
        circuit_to_boxes[i] = {boxes[i]}
        for j in range(i+1, len(boxes)):
            box_pairs.append([boxes[i], boxes[j], distance_between(boxes[i], boxes[j])])
    print("Initial assignments")
    print("box_to_cir", box_to_circuit)
    print("cur_to_boxes", circuit_to_boxes)
    # sort box pairs by distance to get the closest PAIRS_TO_CONSIDER pairs
    box_pairs = sorted(box_pairs, key=lambda x: x[-1])
    for pair in box_pairs[:PAIRS_TO_CONSIDER]:
        first_cir = box_to_circuit[pair[0]]
        second_cir = box_to_circuit[pair[1]]
        # nothing happens if in the same cir
        if first_cir == second_cir:
            continue
        # otherwise, move all boxes from second circuit into the first
        for box in circuit_to_boxes[second_cir]:
            circuit_to_boxes[first_cir].add(box)
            box_to_circuit[box] = first_cir
        circuit_to_boxes[second_cir] = set()

    # once we have the groups, find the NUM_LARGEST largest groups
    # top_3 stores the three largest groups in ascending order
    top_3 = [0] * NUM_LARGEST
    for cir_idx in circuit_to_boxes:
        circuit_size = len(circuit_to_boxes[cir_idx])
        idx = len(top_3) - 1
        to_compare = circuit_size
        while idx >= 0:
            if to_compare > top_3[idx]:
                top_3[idx], to_compare = to_compare, top_3[idx]
            idx -= 1

    tot = top_3[0]
    for group in top_3[1:]:
        tot *= group
    return tot

if __name__ == "__main__":
    input_path = "input.txt"
    # input_path = "small_input.txt"
    boxes = read_input(input_path)
    output = solution(boxes)
    print("output = ", output)
