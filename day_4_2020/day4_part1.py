
from typing import TextIO, Dict
import pprint

def clean_data(input_file: str) -> Dict[str, str]:
	
	# Take the inputfile and clean the file from spaces and blanc lines, split a string into a list.

	input_file = open(input_file, 'r').read()
	input_file = input_file.split('\n\n')
	input_file = [x.replace('\n', ' ').replace(' ', '\n') for x in input_file]
	input_file = [x.split('\n') for x in input_file]
	
	nested_dictionary = dict()

	i = 0

	for passport in input_file:
		external_dictionary = 'dictionary{0}'.format(i)
		internal_dictionary = dict()

		for key_value in passport:
			if len(key_value) != 0:
				key, value = key_value.split(':')
				internal_dictionary.update({key:value})

		nested_dictionary.update({external_dictionary: internal_dictionary})
			
		i += 1
		
	return nested_dictionary

#result = clean_data('day4_input.txt')
#pp = pprint.PrettyPrinter(depth=4)
#pp.pprint(result)

def validator(passport: dict, required_fields: list) -> int:

	result = 1

	for field in required_fields:

		if field not in passport.keys():

			result = 0
			break

	return result


required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# input one
passports = clean_data('day4_input.txt')

valid_passports = []

for passport in passports.values():
    valid_passports.append(validator(passport, required_fields))
#print(valid_passports)

results = sum(valid_passports)
print(results)


