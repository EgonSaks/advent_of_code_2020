map_list = open('day3_input.txt', 'r')

tree_map = [x.strip() for x in map_list.readlines()]

def trees(tree_map):
	'''
	Counting all the trees you would encounter for the slope right 3, down 1
	'''
	
	# Get the size of map
	nr_or_rows = len(tree_map[0])
	nr_of_columns = len(tree_map)
	
	print(f'Field has {nr_of_columns} columns and {nr_or_rows} rows')
	print('_________________________')

	# Current position 
	position = 0

	# Count trees
	count_of_trees = 0
	
	# Go over the each row, look for the row and current position of '#' and if there is '#' count it in and move to the next row 3 steps to the right from past position 
	for row in range(nr_of_columns):
		if tree_map[row][position] == '#':
			count_of_trees +=1
		position = (position + 3) % nr_or_rows
	
	return count_of_trees

# Print how many trees are on the way
print(trees(tree_map))

