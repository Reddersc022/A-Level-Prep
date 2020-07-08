import json

print("*** Data Entry ***")

confirm = False
while not confirm:
	name, dob, num = input("Name: "), input("Date of birth: "), input("Member number: ")
	print("""
	Name   | %s
	DOB    | %s
	Number | %s
	""" % (name, dob, num))
	confirm = True if input("Done? (yes/no) ").lower() == 'yes' else False

with open("Data Entry.json", 'r') as f:
	users = json.load(f)

users.append([name, dob, num])

with open("Data Entry.json", 'w') as f:
	json.dump(users, f)

for i in users:
	print("""
	Name   | %s
	DOB    | %s
	Number | %s
	""" % (i[0], i[1], i[2]))
