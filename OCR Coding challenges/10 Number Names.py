from num2words import num2words

print("*** Number names ***")

n = int(input("Number: "))
print("%d is %s" % (n, num2words(n)))
