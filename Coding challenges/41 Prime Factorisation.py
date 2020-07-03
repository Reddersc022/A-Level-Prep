print("*** Prime Factorisation ***")


n = int(input("Number: "))

i, factors = 1, []
while i * i <= n:
	if n % i:
		i += 1
	else:
		n //= i
		factors.append(i)
if n > 1:
	factors.append(n)

print(factors)
