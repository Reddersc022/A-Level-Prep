print("*** Simple Life Calculator ***")


def main():
	choice = int(input("""
	1. VAT
	2. Income Tax
	3. Times Tables
	4. Exit\n: """))

	if choice == 4:
		exit()

	if choice == 1:
		print("Vat | %f" % round((int(input("Price: ")) * 1.2), 2))
	elif choice == 2:
		income = int(input("Income: "))
		if income <= 12500:
			final = income
		elif 12501 <= income <= 50000:
			final = 12500 + (income - 12500) * .8
		elif 50001 <= income <= 150000:
			final = 12500 + 30000 + (income - 12500 - 50000) * .6
		else:
			final = 12500 + 30000 + 55000 + (income - 12500 - 50000 - 100000) * .55

		print("Income after tax: %d" % final)  # Note: purely tax - not including national insurance, etc..
	elif choice == 3:
		print(int(input("Number 1: ")) * int(input("Number 2: ")))

	main()


main()
