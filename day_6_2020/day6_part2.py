questions = open("day6_input.txt", "r").read()
def questions_to_which_everyone_answered_yes(questions):

	questions = questions.split("\n\n")
	questions = [question.splitlines() for question in questions]

	questions_to_which_everyone_answered_yes = 0

	for group in questions:
		#print(group)
		main_set = set(group[0])
		#print(main_set)
		for people in group[1:]:
			main_set = main_set.intersection(set(people))
			print(main_set)

		questions_to_which_everyone_answered_yes += len(main_set)
		
	return questions_to_which_everyone_answered_yes

everyone_answered_yes = questions_to_which_everyone_answered_yes(questions)

print(f"The number of questions to which everyone answered 'yes' is: {everyone_answered_yes}")


