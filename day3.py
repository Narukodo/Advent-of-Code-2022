with open('day3_inputs.txt') as f:
    rucksacks_combined = f.read().splitlines()
    rucksacks = [[rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]] for rucksack in rucksacks_combined]

combined_priority = 0
# day 1
for [comp1, comp2] in rucksacks:
    comp1_dedup = set(comp1)
    comp2_dedup = set(comp2)
    shared_items = comp1_dedup.intersection(comp2_dedup)
    for item in shared_items:
        if item.islower():
            combined_priority += ord(item) - 96
        else:
            combined_priority += ord(item) - 38

print(combined_priority)

combined_group_priorities = 0
# day 2
rucksack_groups = [rucksacks_combined[i * 3:(i + 1) * 3] for i in range((len(rucksacks_combined) + 2) // 3 )]
for [elf1_rucksack, elf2_rucksack, elf3_rucksack] in rucksack_groups:
    elf1_rucksack_types = set(elf1_rucksack)
    elf2_rucksack_types = set(elf2_rucksack)
    elf3_rucksack_types = set(elf3_rucksack)
    items_elves_share = elf1_rucksack_types.intersection(elf2_rucksack_types, elf3_rucksack_types)
    for item in items_elves_share:
        if item.islower():
            combined_group_priorities += ord(item) - 96
        else:
            combined_group_priorities += ord(item) - 38

print(combined_group_priorities)