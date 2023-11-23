test = [[3,0,3,7,3],
[2,5,5,1,2],
[6,5,3,3,2],
[3,3,5,4,9],
[3,5,3,9,0]]
with open('day8_input.txt') as f:
    rows = f.read().splitlines()
    rows = [[int(height) for height in list(row)] for row in rows]
    columns = list(zip(*rows))
    is_visible = [[False for i in range(len(row))] for row in columns]
    num_visible_trees = len(rows) * 2 + len(rows[0]) * 2 - 4
    for height_index, height in enumerate(is_visible[0]):
        is_visible[0][height_index] = True
    for height_index, height in enumerate(is_visible[-1]):
        is_visible[-1][height_index] = True
    for row_index, row in enumerate(is_visible):
        is_visible[row_index][0] = True
        is_visible[row_index][-1] = True

    forest_width = len(rows[0])
    forest_length = len(rows)
    
    for row_index, row in enumerate(rows):
        # check from left
        highest_tree = row[0]
        for height_index, height in enumerate(row):
            if height > highest_tree:
                highest_tree = height
                if not is_visible[row_index][height_index]:
                    num_visible_trees += 1
                    is_visible[row_index][height_index] = True
        
        # check from right
        highest_tree = row[-1]
        for height_index, height in enumerate(row[::-1]):
            if height > highest_tree:
                highest_tree = height
                if not is_visible[row_index][forest_width - height_index - 1]:
                    num_visible_trees += 1
                    is_visible[row_index][forest_width - height_index - 1] = True
    for col_index, column in enumerate(columns):
        highest_tree = column[0]
        for height_index, height in enumerate(column):
            if height > highest_tree:
                highest_tree = height
                if not is_visible[height_index][col_index]:
                    num_visible_trees += 1
                    is_visible[height_index][col_index] = True
        
        highest_tree = column[-1]
        for height_index, height in enumerate(column[::-1]):
            if height > highest_tree:
                highest_tree = height
                if not is_visible[forest_length - height_index - 1][col_index]:
                    num_visible_trees += 1
                    is_visible[forest_length - height_index - 1][col_index] = True
            