import json
import random

print("*** Quiz Maker ***")

grading = {5: 'A', 4: 'B', 3: 'C', 2: 'D', 1: 'E', 0: 'F'}

with open("Quiz Maker.json", 'r') as f:
	lst = json.load(f)

questions = []
for __ in range(5):
	question = random.choice(lst)
	lst.remove(question)
	questions.append(question)

score = 0
for question in questions:
	if input(question[0]+"\n: ").lower() == question[1]:
		print("Correct")
		score += 1
	else:
		print("Incorrect")

print("You got %d/5: %s" % (score, grading[score]))
