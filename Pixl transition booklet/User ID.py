# User ID

fullName = input("Full name: ")
while not (fullName.replace(' ', '')).isalpha():
	fullName = input("Full name (all letters): ")
	if fullName.lower() == 'quit':
		exit()
space = fullName.index(' ')

dob = input("Date of birth: ")
while not dob.isnumeric() or len(dob) != 8:
	dob = input("Date of birth (ddmmyyyy): ")
	if dob.lower() == 'quit':
		exit()

print("User ID: %s%d" % (dob[4:]+dob[2:4]+dob[:2]+fullName[space+1:space+4].upper()+fullName[0], len(fullName[:space])))
