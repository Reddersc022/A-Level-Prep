# Products

lst = []
while True:
	product, price = input("Product: "), int(input("Price: "))
	if product.lower() == "none":
		break
	lst.append([product, price])
lst.sort(key=lambda x: x[1])

print("Dearest: %s\nCheapest: %s\nAverage price: %d" % (lst[-1], lst[0],
	sum([i[1]*1.2 if i[1] < 50 else i[1] * 1.14 for i in lst])/len(lst)))
