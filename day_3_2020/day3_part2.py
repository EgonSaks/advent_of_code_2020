map_list = open('day3_input.txt', 'r')

tree_map = [x.strip() for x in map_list.readlines()]

def trees(tree_map):
	def more_trees(right, down):
		'''
		Counting all the trees you would encounter for the slopes:
		- Right 1, Down 1, 
		- Right 3, Down 1, 
		- Right 5, Down 1, 
		- Right 7, Down 1, 
		- Right 1, Down 2
		'''
		
		# Current position 
		position = 0

		# Count trees
		count_of_trees = 0
		
		# Go over the each row, look if is doesn't equal '0' continue, if row and current position is '#' and if there is '#' count it in and move to the next row on given steps to the right from past position 
		for row in range(len(tree_map)):
			if row % down != 0:
				continue
			if tree_map[row][position] == '#':
				count_of_trees +=1
			position = (position + right) % len(tree_map[0])		
		return count_of_trees

	
	# Print how many trees are on the way
	one_on_one = more_trees(1,1)
	three_on_one = more_trees(3,1)
	five_on_one = more_trees(5,1)
	seven_on_one = more_trees(7,1)
	one_on_one = more_trees(1,1)

	print(f'Road has {one_on_one} trees on the way')
	print('_________________________')
	print(f'Road has {three_on_one} trees on the way')
	print('_________________________')
	print(f'Road has {five_on_one} trees on the way')
	print('_________________________')
	print(f'Road has {seven_on_one} trees on the way')
	print('_________________________')
	print(f'Road has {one_on_one} trees on the way')
	print('_________________________')

	return more_trees(1,1) * more_trees(3,1) * more_trees(5,1) * more_trees(7,1) * more_trees(1,2)

encountere_slopes = trees(tree_map)
print(f'Number of trees encountered on each of the listed slopes is {encountere_slopes}')

