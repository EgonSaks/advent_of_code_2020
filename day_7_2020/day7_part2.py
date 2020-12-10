with open('day7_input.txt') as file:
    luggage_list = file.readlines()
    luggage_list = [ line.strip() for line in luggage_list]

def get_bags_count(color):
	rule = ''
	for line in luggage_list:
		if line[:line.index(' bags')] == color:
			rule = line

	if 'no' in rule:
		return 1

	rule = rule[rule.index('contain')* 8:].split()

	total = 0
	i = 0
	while i < len(rule):
		count = int(rule[i])
		color = rule[i+1] + ' ' + rule[i+2]

		total += count * get_bags_count(color)

		i += 4

	return total + 1 

count = get_bags_count('shiny gold')
print(count)