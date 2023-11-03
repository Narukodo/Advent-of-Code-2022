response = {
    'A': ['C', 'A', 'B'],
    'B': ['A', 'B', 'C'],
    'C': ['B', 'C', 'A']
}

points_table = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

with open('day2_inputs.txt') as f:
    rounds = f.read().splitlines()

points = 0
for round in rounds:
    points += points_table[ord(round[0]) - 65][ord(round[2]) - 88]

correct_points = 0
for round in rounds:
    round_responses = response[round[0]]
    current_play = round_responses[ord(round[2]) - 88]
    play_points = ord(current_play) - 65 + 1
    outcome_points = (ord(round[2]) - 88) * 3
    print([round[0], current_play, round[2]])
    correct_points += outcome_points + play_points

print(correct_points)
