print("*** Happy Numbers ***")

n = int(input("Number: "))

x, current, last = n, 0, 1
while current != last:
	x = sum([int(i) for i in str(x)])
	last = current
	current = x

print("%d is %s" % (n, "happy" if x == 1 else "unhappy"))
