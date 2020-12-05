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
    # This method is the same as before but with the data validation rules.
    result = 1
    broke_reason = []

    for field in required_fields:

        try:

            if field not in passport.keys():

                result = 0
                broke_reason.append('not_present')
                break

            # byr validator
            if field == 'byr':

                byr = int(passport[field])
				# Check if byr is four digits
                if len(str(byr)) != 4:
                    result = 0
                    broke_reason.append('byr not 4')
				# Checkt if byr is at least 1920 and at most 2002.
                if (byr < 1920) or (byr > 2002):
                    broke_reason.append('byr out of range')
                    result = 0

            # iyr validator
            if field == 'iyr':
				
                iyr = int(passport[field])
				# Check if iyr is four digits
                if len(str(iyr)) != 4:
                    broke_reason.append('iyr not 4')
                    result = 0
				# Checkt if iyr is at least 2010 and at most 2020
                if (iyr < 2010) or (iyr > 2020):
                    broke_reason.append('iyr out of range')
                    result = 0

            # eyr validator
            if field == 'eyr':
				
                eyr = int(passport[field])
				# Check if iyr is four digits
                if len(str(eyr)) != 4:
                    broke_reason.append('eyr not 4')
                    result = 0
                    # Checkt if eyr is at least 2020 and at most 2030.
                if (eyr < 2020) or (eyr > 2030):

                    broke_reason.append('eyr out of range')
                    result = 0
                    
            # hgt validator
            if field == 'hgt':

                hgt = str(passport[field])
				# Check if a number followed by either cm
                if 'cm' in hgt:

                    hgt_value = hgt.replace('cm', '')
                    if hgt_value != '':
                        hgt_value = int(hgt_value)
						# If cm, the number must be at least 150 and at most 193.
                        if (hgt_value < 150) or (hgt_value > 193):
                            broke_reason.append('hgt cm out of range')
                            result = 0
                            
                elif 'in' in hgt:

                    hgt_value = hgt.replace('in', '')
                    if hgt_value != '':
                        hgt_value = int(hgt_value)
						# If in, the number must be at least 59 and at most 76.
                        if (hgt_value < 59) or (hgt_value > 76):
                            broke_reason.append('hgt in out of range')
                            result = 0
                            # break
                else:
                    result = 0
                    broke_reason.append('hgt no in or cm')

            if field == 'hcl':

                valid_characters = ['0', '1', '2', '3', '4', '5',
                                    '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

                hcl = str(passport[field])
				# a # followed by exactly six characters 0-9 or a-f.
                if '#' not in hcl:
                    broke_reason.append('hcl no #')
                    result = 0

                if len(hcl) != 7:
                    broke_reason.append('hcl not 7')
                    result = 0

                for char in hcl[1:]:
                    if char not in valid_characters:
                        broke_reason.append('hcl invalid char: {}'.format(char))
                        result = 0

            if field == 'ecl':

                ecl = str(passport[field])
                valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
				# If exactly one of: amb blu brn gry grn hzl oth.
                if len(ecl) != 3:
                    broke_reason.append('ecl not 3')
                    result = 0

                if ecl not in valid_colors:
                    broke_reason.append('ecl not valid color')
                    result = 0

            if field == 'pid':
				# if a nine-digit number, including leading zeroes
                pid = str(passport[field])
				
                if len(pid) != 9:
                    broke_reason.append('pid not 9')
                    result = 0
        except Exception as e:
            print(passport, e)

    # return (result, broke_reason)
    return result

# 
required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  

# Call the cleaned data function and get back cleaned data as nested_dictionary
passports = clean_data('day4_input.txt')

valid_passports = []

# Loop through passports for passport and call the validator to validate if passports have all the required fields, return 1 if yes 0 if no
for passport in passports.values():
    valid_passports.append(validator(passport, required_fields))

result = sum(valid_passports)
print(result)