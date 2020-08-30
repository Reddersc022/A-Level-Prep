import random

print("*** Of Mice and Men ***")

number = [random.randint(0, 9) for _ in range(4)]
print(number)

while True:
	guess = list(map(int, list(input("Guess: "))))

	if guess == number:
		print("Well done!")
		break

	men, mice = 0, 0
	for a, b in zip(number, guess):
		if a == b:
			mice += 1
		elif a in number:
			men += 1

	print("Mice: %d \nMen: %d" % (mice, men))
