print("*** Spam Filter ***")

dishes = [input("Dish %d: " % i).split() for i in range(int(input("How many dishes: ")))]

for i in dishes:
	sep = list(map(lambda x: x.replace(",", ""), [j for j in i if j != "and"]))
	print(", ".join(sep) + ", and Spam")
