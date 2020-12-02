# Get the input
password_list = open('day2_input.txt', 'r')

# Remove spaces
passwords = [x.strip() for x in password_list.readlines()]

# Split string into a list, convert first part of string to int for minimum and maximu given letter count, count given letter in password, return nr of passwords where minimum or maximum conditions are met.
def letter_count(passwords):

	nr_of_correct_passwords = 0

	for x in passwords:
		nr, letter, password = x.split()
		minimum, maximum = map(int, nr.split('-'))

		count_letter = password.count(letter[0])

		if minimum <= count_letter <= maximum:
			nr_of_correct_passwords += 1 

	return nr_of_correct_passwords
			
print(letter_count(passwords))