import requests
from requests.exceptions import HTTPError

# The response object below can be removed if an actual POST request will be made which 
# would have a valid response.
response = {
		    'quizSubject': [{
		        'sports': [{
		            'q1': {
		                'question': 'Which one is correct team name in NBA?',
		                'options': [
		                    "New York Bulls",
		                    "Los Angeles Kings",
		                    "Golden State Warriors",
		                    "Houston Rocket"
		                ],
		                'answer': "Houston Rocket"
		            }
		        }]
		    }, {
		        'math': [{
		            'q1': {
		                'question': '5 + 7 = ?',
		                'options': [
		                    "10",
		                    "11",
		                    "12",
		                    "13"
		                ],
		                'answer': '12'
		            }
		        }, {
		            'q2': {
		                'question': '12 - 8 = ?',
		                'options': [
		                    "1",
		                    "2",
		                    "3",
		                    "4"
		                ],
		                'answer': '4'
		            }
		        }]
		    }]
		}



def validate_options(subject, ind):
	res = []
	if(s[ind] in subject.keys()):
		if(len(subject[s[ind]]) >= 1):
			for question in range(len(subject[s[ind]])):
				options = list(subject[s[ind]][question].values())[0]['options']
				if(not options):
					res.append((list(subject.keys())[0],list(subject[s[ind]][ind]), "Invalid"))
				else:
					if(len(options) == 4 and None not in options):
						res.append((list(subject.keys())[0], list(subject[s[ind]][question])[0],"Valid"))
					else:
						res.append((list(subject.keys())[0], list(subject[s[ind]][ind]),"Invalid"))
		else:
			res.append((list(subject.keys())[0],list(subject[s[ind]][ind]), "Invalid"))
	return res

def validate_sports(sports):
	# To answer this question, the logic used take care of the case where the elemets will be in
	# a different order. 
	ref_list = ["New York Bulls", "Los Angeles Kings", "Golden State Warriors", "Houston Rocket"]
	for sub in range(len(response['quizSubject'])):
		if('sports' in response['quizSubject'][sub].keys()):
			sports_list = response['quizSubject'][0]['sports'][0]['q1']['options']
			if not sports_list:
				return "Invalid"
			else:
				for team in sports_list:
					if team in ref_list:
						ref_list.remove(team)
	return ref_list == []



if __name__ == "__main__":

	url = "https://validate.test.com/api/quiz-questions"
	payload = {"quizSubject": ["sports", "math"],"semester": "2"}
	s = payload["quizSubject"]
	result = []

	try:
		response = response

		#The following two lines are commented because an actual post request will
		#not be made here

		#response = requests.post(url, data = payload)
		#response.raise_for_status()
	except HTTPError as http_err:
	        print(f'HTTP error occurred: {http_err}')
	except Exception as err:
	        print(f'Other error occurred: {err}')


	else:
		quiz_subjects = response['quizSubject']
		# Solution for Part 1 of the Question
		for sub in range(len(quiz_subjects)):
			subjects = quiz_subjects[sub]
			result.append(validate_options(subjects, sub))
		print(result)

		# Solution for Part 2 of the Question
		sports_valid = validate_sports(quiz_subjects)
		print("Options in sports are", "Valid" if sports_valid else "Invalid")


