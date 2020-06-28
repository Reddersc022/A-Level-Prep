import json
import random

print("*** Quiz Maker ***")

grading = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1, 'F': 0}

with open("Quiz Maker.json", 'r') as f:
	lst = json.load(f)

questions = []
for __ in range(5):
	question = random.choice(lst)
	lst.remove(question)
	questions.append(question)

score = 0

