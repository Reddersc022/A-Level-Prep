print("*** Year Addition ***")

n = sum([int(i) for i in input("Year: ")])
for __ in range(3):
	if n % int(input("Guess: ")) == 0:
		print("Correct")
		break
	else:
		print("Incorrect")
