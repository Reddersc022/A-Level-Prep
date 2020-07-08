import random
import json

print("*** Arithmetic Test ***")

scores = []
for __ in range(10):
	question = "%d %s %d" % (random.randint(0, 9), random.choice(["+", "-", "*", "/"]), random.randint(0, 9))
	if float(input("%s = " % question)) == float(eval(question)):
		print("Correct")
		scores.append(1)
	else:
		print("Incorrect")
		scores.append(0)

print("Score = %d" % sum(scores))

with open("Arithmetic Test.json", "r") as f:
	lst = json.load(f)

lst.append([input("Name: "), sum(scores), scores])

with open("Arithmetic Test.json", "w") as f:
	json.dump(lst, f)

lst.sort(reverse=True, key=lambda x: sum(x[2][7:]))
print("The best, based on last 3 scores, are: \n%s" % ''.join([i[0]+" \n" for i in lst]))
