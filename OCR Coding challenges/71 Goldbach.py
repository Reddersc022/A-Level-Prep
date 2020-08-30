print("*** Goldbach ***")

# For sum of primes < 100

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
num = int(input(":: "))

for i in primes:
	for j in primes:
		if i + j == num:
			print("%d + %d = %d" % (i, j, num))
