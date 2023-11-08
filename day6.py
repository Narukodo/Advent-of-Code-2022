with open('day6_input.txt') as f:
    datastream = f.read()

total_characters = len(datastream)

for i in range(total_characters):
    if len(set(datastream[i:i + 4])) == 4:
        print(i + 4)
        break

for i in range(total_characters):
    if len(set(datastream[i: i+14])) == 14:
        print(i + 14)
        break