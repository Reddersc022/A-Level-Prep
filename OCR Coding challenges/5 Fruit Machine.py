import random

print("*** Fruit Machine ***")

credit = 1
while True:
	credit = round(credit, 2) - .2
	if credit < 0 or input("Stop? (y/n) ").lower() == 'y':
		break
	f1, f2, f3 = random.choice(['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']), \
		random.choice(['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull']), \
		random.choice(['Cherry', 'Bell', 'Lemon', 'Orange', 'Star', 'Skull'])
	if f1 == f2 and f1 == f3:
		if f1 == 'Bell':
			credit += 5
		elif f1 == 'Skull':
			credit = 0
		else:
			credit += 1
	elif f1 == f2 or f2 == f3 or f1 == f3:
		if f1 == 'Skull' or f2 == 'Skull':
			credit -= 1
		else:
			credit += .5
	print("Credit:", credit)
