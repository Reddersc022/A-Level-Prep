print("*** Classification ***")

# Climbing holds

indent, fingers, curved, big = bool(input("Indent: ")), bool(input("Fingers: ")), bool(input("Curved: ")), bool(input("Big: "))

if indent:
	if fingers == 1:
		print('Mono')
	else:
		if curved:
			if big:
				print('Jug')
			else:
				print('Pocket')
		else:
			print('Slot')
else:
	if curved:
		if big:
			print('Sloper')
		else:
			print('Pinch')
	else:
		print('Crimp')
