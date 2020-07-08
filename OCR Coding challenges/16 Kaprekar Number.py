print("*** Kaprekar Number ***")

num = int(input("Number: "))

if num == 1:
	print("Kaprekar")
elif (num**2) < 15:
	print("Not Kaprekar")

stringNum = str(num ** 2)
if num == int(stringNum[:len(stringNum) // 2]) + int(stringNum[len(stringNum) // 2:]):
	print("Kaprekar")
else:
	print("Not Kaprekar")
