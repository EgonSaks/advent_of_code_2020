# Get the input
password_list = open('day2_input.txt', 'r')

# Remove spaces
passwords = [x.strip() for x in password_list.readlines()]


def checking_positions_in_the_password(passwords):
	''' Split string into a list, convert first part of string to int for positions of given letter count, check  return nr of passwords where minimum or maximum conditions are met.'''
	nr_of_passwords = 0

	for x in passwords:
		nr, letter, password = x.split()
		minimum, maximum = map(int, nr.split('-'))

		# Two positions in the password, 1 means the first character, 2 means the second character, and so on. Checking if one of these positions contains the given letter. No concept of "index zero" 
		position1 = password[minimum-1] == letter[0]
		position2 = password[maximum-1] == letter[0]


		# Other occurrences of the letter are irrelevant for the purposes of policy enforcement
		if position1 != position2:
			nr_of_passwords += 1 

	return nr_of_passwords
			
print(checking_positions_in_the_password(passwords))