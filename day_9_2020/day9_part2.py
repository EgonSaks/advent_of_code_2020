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
#print(not_the_sum)

def get_encryption_weakness(not_the_sum, xmas):
    for i in range(len(xmas)):
        sum, min, max = xmas[i], xmas[i], xmas[i]

        for j in range(i + 1, len(xmas)):
            current = xmas[j]
            sum, min, max = (sum + current), (min if min < current else current), (max if max > current else current)

            if sum > not_the_sum:
                break
            elif sum == not_the_sum:
                return min + max

print(get_encryption_weakness(not_the_sum, xmax))