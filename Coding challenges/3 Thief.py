import itertools

print("*** Thief ***")

lst = [int(input("Number 1: ")), int(input("Number 2: ")), int(input("Number 3: ")), int(input("Number 4: "))]

for i in itertools.permutations(lst):
	print(i)
