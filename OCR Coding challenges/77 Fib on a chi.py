print("*** Fib on a chi ***")

back2, back1 = 1, 1

while True:
	current = back1 + back2
	if len(str(current)) == 1000:
		print(current)
		break
	back1, back2 = current, back1
