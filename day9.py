test = [['R', 4],
['U', 4],
['L', 3],
['D', 1],
['R', 4],
['D', 1],
['L', 5],
['R', 2]
]
def parse_input():
    with open('day9_input.txt') as f:
        steps = [step.split(' ') for step in f.read().splitlines()]
        steps = [[step[0], int(step[1])] for step in steps]
        return steps

def is_adjacent(pos_head, pos_tail):
    head_y, head_x = pos_head
    tail_y, tail_x = pos_tail
    return -1 <= head_x - tail_x and 1 >= head_x - tail_x and -1 <= head_y - tail_y and 1 >= head_y - tail_y

def move_knot(pos_head, pos_tail):
    head_y, head_x = pos_head
    tail_y, tail_x = pos_tail
    # tail can move in one of 8 directions
    if head_x > tail_x and head_y == tail_y:
        return [tail_y, tail_x + 1]
    if head_x < tail_x and head_y == tail_y:
        return [tail_y, tail_x - 1]
    if head_x == tail_x and head_y > tail_y:
        return [tail_y + 1, tail_x]
    if head_x == tail_x and head_y < tail_y:
        return [tail_y - 1, tail_x]
    if head_x < tail_x and head_y < tail_y:
        return [tail_y - 1, tail_x - 1]
    if head_x < tail_x and head_y > tail_y:
        return [tail_y + 1, tail_x - 1]
    if head_x > tail_x and head_y < tail_y:
        return [tail_y - 1, tail_x + 1]
    if head_x > tail_x and head_y > tail_y:
        return [tail_y + 1, tail_x + 1]

def move_head(pos_head, direction):
    head_y, head_x = pos_head
    if direction == 'R':
        return [head_y, head_x + 1]
    if direction == 'L':
        return [head_y, head_x - 1]
    if direction == 'D':
        return [head_y + 1, head_x]
    if direction == 'U':
        return [head_y - 1, head_x]

def simulate_movements():
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited_positions = {0:{0}}
    num_visited_positions = 0
    # steps = test
    steps = parse_input()

    for direction, distance in steps:
        num_steps_left = distance
        while num_steps_left > 0:
            head_pos = move_head(head_pos, direction)
            if not is_adjacent(head_pos, tail_pos):
                tail_pos = move_knot(head_pos, tail_pos)
                if tail_pos[0] in visited_positions:
                    visited_positions[tail_pos[0]].add(tail_pos[1])
                else:
                    visited_positions[tail_pos[0]] = {tail_pos[1]}
            num_steps_left -= 1
    for y in visited_positions:
        num_visited_positions += len(visited_positions[y])
    return num_visited_positions

print(simulate_movements())


