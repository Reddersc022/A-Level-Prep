print("*** Mortgage Calculator ***")

totalAmount, years, compoundingInterval, interest = int(input("Total, initial amount: ")), \
	int(input("Years of mortgage: ")), input("Compounding interval (month or year): "), int(input("Interest: "))

totalOverTime = totalAmount * pow(1 + (interest / 100), years)
print("You will pay %.2f each %s, meaning a total of %d" %
	(totalOverTime / (years * (12 if compoundingInterval == "month" else 1)), compoundingInterval, totalOverTime))


