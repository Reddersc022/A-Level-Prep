import random
import json

print("*** Hack Proof ***")

with open("Hack Proof.json", 'r') as f:
	l = json.load(f)

if not l:
	pwd = ''.join([random.choice([chr(i) for i in range(65, 123)]) for __ in range(9)])
	suggested = input("Suggested password: %s \nDo you want to use it? (yes/no) " % pwd)
	if suggested == 'yes':
		confirm = True
	else:
		confirm = False

	while not confirm:
		pwd = input("Enter your password: ")
		lst = [False, False, False]
		for i in pwd:
			if i.isnumeric():
				lst[0] = True
			elif i.isupper():
				lst[1] = True
			elif not (i.isnumeric() or i.isalpha()):
				lst[2] = True
		confirm = True if lst == [True, True, True] else False

	with open("Hack Proof.json", "w") as f:
		json.dump([input("Username: "), pwd], f)
else:
	if [input("Username: "), input("Password: ")] == l:
		with open("Hack proof.txt", 'r') as f:
			print(f.read())
	else:
		print("Incorrect details")
