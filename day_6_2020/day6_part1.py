

questions = open("day6_input.txt", "r").read()
def count_of_yes_questions(questions):	
	
	#Clean up the data and make a count of yes answers
	
	questions = questions.split("\n\n")
	questions = [question.replace("\n", "") for question in questions]

	questions = [list(set(question)) for question in questions] # set() in list to keep only unique questions where answer was yes
	questions = [len(question) for question in questions] # count of unique questions
	questions = sum(questions) # sum of unique questions
	return questions

yes = count_of_yes_questions(questions)

print(f"Count the number of questions to which anyone answered 'yes' is: {yes}")
