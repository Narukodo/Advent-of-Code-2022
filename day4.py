with open('day4_inputs.txt') as f:
    pair_assignments = f.read().splitlines()
    pair_assignments = [pair_assignment.split(',') for pair_assignment in pair_assignments]
    pair_assignments = [[range1.split('-'), range2.split('-')] for [range1, range2] in pair_assignments]
    pair_assignments = [[[int(range1[0]), int(range1[1])], [int(range2[0]), int(range2[1])]] for [range1, range2] in pair_assignments]
    # assignments = [assignment for pair in pair_assignments for assignment in pair]

overlapped_pairs = 0
for [elf1, elf2] in pair_assignments:
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]):
        overlapped_pairs += 1

print(overlapped_pairs)

# part 2
# sorted_assignments = sorted(assignments)
# open_interval = sorted_assignments[0]
# overlapping_assignments = 0
# for [start, end] in sorted_assignments:
#     if start < open_interval[1]:
#         overlapping_assignments += 

overlapping_pairs = 0

def is_overlapping(interval1, interval2):
    [ax, ay] = interval1
    [bx, by] = interval2
    if (bx <= ay and ay <= by) or (bx <= ax and ax <= by) or (ax <= by and by <= ay) or (ax <= bx and bx <= ay):
        return True
    return False

for [elf1, elf2] in pair_assignments:
    if is_overlapping(elf1, elf2) or is_overlapping(elf2, elf1):
        overlapping_pairs += 1

print(overlapping_pairs)
