with open('q1_inputs.txt') as f:
    calories_total = f.read().splitlines()
    highest_calories = 0
    i = 0
    num_of_lines = len(calories_total)
    current_calories = 0
    while i < num_of_lines:
        if len(calories_total[i]) > 0:
            current_calories += int(calories_total[i])
        else:
            highest_calories = max(highest_calories, current_calories)
            current_calories = 0
        i += 1
        
print(highest_calories)