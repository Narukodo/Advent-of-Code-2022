import math

test = [
['addx', 15],
['addx', -11],
['addx', 6],
['addx', -3],
['addx', 5],
['addx', -1],
['addx', -8],
['addx', 13],
['addx', 4],
['noop',],
['addx', -1],
['addx', 5],
['addx', -1],
['addx', 5],
['addx', -1],
['addx', 5],
['addx', -1],
['addx', 5],
['addx', -1],
['addx', -35],
['addx', 1],
['addx', 24],
['addx', -19],
['addx', 1],
['addx', 16],
['addx', -11],
['noop',],
['noop',],
['addx', 21],
['addx', -15],
['noop',],
['noop',],
['addx', -3],
['addx', 9],
['addx', 1],
['addx', -3],
['addx', 8],
['addx', 1],
['addx', 5],
['noop',],
['noop',],
['noop',],
['noop',],
['noop',],
['addx', -36],
['noop',],
['addx', 1],
['addx', 7],
['noop',],
['noop',],
['noop',],
['addx', 2],
['addx', 6],
['noop',],
['noop',],
['noop',],
['noop',],
['noop',],
['addx', 1],
['noop',],
['noop',],
['addx', 7],
['addx', 1],
['noop',],
['addx', -13],
['addx', 13],
['addx', 7],
['noop',],
['addx', 1],
['addx', -33],
['noop',],
['noop',],
['noop',],
['addx', 2],
['noop',],
['noop',],
['noop',],
['addx', 8],
['noop',],
['addx', -1],
['addx', 2],
['addx', 1],
['noop',],
['addx', 17],
['addx', -9],
['addx', 1],
['addx', 1],
['addx', -3],
['addx', 11],
['noop',],
['noop',],
['addx', 1],
['noop',],
['addx', 1],
['noop',],
['noop',],
['addx', -13],
['addx', -19],
['addx', 1],
['addx', 3],
['addx', 26],
['addx', -30],
['addx', 12],
['addx', -1],
['addx', 3],
['addx', 1],
['noop',],
['noop',],
['noop',],
['addx', -9],
['addx', 18],
['addx', 1],
['addx', 2],
['noop',],
['noop',],
['addx', 9],
['noop',],
['noop',],
['noop',],
['addx', -1],
['addx', 2],
['addx', -37],
['addx', 1],
['addx', 3],
['noop',],
['addx', 15],
['addx', -21],
['addx', 22],
['addx', -6],
['addx', 1],
['noop',],
['addx', 2],
['addx', 1],
['noop',],
['addx', -10],
['noop',],
['noop',],
['addx', 20],
['addx', 1],
['addx', 2],
['addx', 2],
['addx', -6],
['addx', -11],
['noop',],
['noop',],
['noop',],
]

def parse_input():
    with open('day10_input.txt') as f:
        operations = [op.split(' ') for op in f.read().splitlines()]
        operations = [[op[0], int(op[1])] if len(op) == 2 else op for op in operations]
        return operations

def move_sprite(new_pos):
    sprite_pos = {new_pos -1, new_pos, new_pos + 1}
    return ['#' if i in sprite_pos else '.' for i in range(40)]

def get_current_pixel(current_cycle, current_state):
    return current_state[current_cycle]

def increase_cycle(cycle):
    cycle += 1
    return cycle, cycle % 40, math.floor(cycle/40)

def simulate_ops():
    x = 1
    cycle_number = 0
    # operations = test
    operations = parse_input()
    cycles_to_track = {20, 60, 100, 140, 180, 220}
    total_signal_strength = 0
    for operation in operations:
        if operation[0] == 'noop':
            cycle_number += 1
            if cycle_number in cycles_to_track:
                total_signal_strength += cycle_number * x
        else:
            value = operation[1]
            cycle_number += 2
            if cycle_number in cycles_to_track:
                total_signal_strength += cycle_number * x
            if cycle_number - 1 in cycles_to_track:
                total_signal_strength += (cycle_number - 1) * x
            x += value
    print(total_signal_strength)

def simulate_sprite():
    operations = parse_input()
    crt_screen = [['.' for i in range(40)] for j in range(6)]
    current_sprite = ['#' if i < 3 else '.' for i in range(40)]
    cycle_number = 0
    x = 1
    for operation in operations:
        current_col = cycle_number % 40
        current_row = math.floor(cycle_number/40)
        if operation[0] == 'addx':
            crt_screen[current_row][current_col] = get_current_pixel(current_col, current_sprite)
            cycle_number, current_col, current_row = increase_cycle(cycle_number)
            crt_screen[current_row][current_col] = get_current_pixel(current_col, current_sprite)
            x += operation[1]
            current_sprite = move_sprite(x)
            cycle_number, current_col, current_row = increase_cycle(cycle_number)
        else:
            crt_screen[current_row][current_col] = get_current_pixel(current_col, current_sprite)
            cycle_number, current_col, current_row = increase_cycle(cycle_number)
    print('\n'.join([''.join(row) for row in crt_screen]))
simulate_sprite()