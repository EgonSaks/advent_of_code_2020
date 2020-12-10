data = 'day9_input.txt'

with open(data) as data:
	data = [int(number) for number in data.read().strip().split("\n")]

	start, step, xmax = 0, 25, data[25:]

end = start + step

def get_sum(data):
    return [nr1 + nr2 for nr1 in data for nr2 in data[1:]]

def not_the_sum_of_two(xmax, start, end, step):
	for number in xmax:
		new_data = get_sum(data[start:end])
		if number not in new_data:
			return number

		start += 1
		end = start + step

not_the_sum = not_the_sum_of_two(xmax, start, end, step)
print(not_the_sum)