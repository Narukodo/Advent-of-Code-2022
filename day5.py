import re

with open('day5_inputs.txt') as f:
    instructions = f.read().splitlines()
    crates = instructions[:10]
    crates = [crate[1::4] for crate in crates][:-2]
    crates.reverse()
    crate_towers = [[] for i in range(len(crates[0]))]
    for row in crates:
        for index, crate in enumerate(row):
            if not crate == ' ':
                crate_towers[index].append(crate)
    instructions = [re.split('move | from | to ', instruction) for instruction in instructions[10:]]
    instructions = [[int(instruction[1]), int(instruction[2]) - 1, int(instruction[3]) - 1] for instruction in instructions]

# day 5 part 1
# for [num_crates, from_crate, to_crate] in instructions:
#     for i in range(num_crates):
#         current_crate = crate_towers[from_crate].pop()
#         crate_towers[to_crate].append(current_crate)

for [num_crates, from_tower, to_tower] in instructions:
    from_tower_height = len(crate_towers[from_tower])
    crate_towers[to_tower] += crate_towers[from_tower][from_tower_height - num_crates:]
    crate_towers[from_tower] = crate_towers[from_tower][:from_tower_height - num_crates]

print(''.join([tower.pop() for tower in crate_towers]))
