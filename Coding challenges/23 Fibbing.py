print("*** Fibbing ***")

n1, n2 = 0, 1
lst = [1]
for i in range(int(input("Range: ")) - 1):
	lst.append(n1+n2)
	n1, n2, = n2, n1+n2

print(''.join("%d, " % i for i in lst)[:-2])
print("Sum: %d" % sum(lst))
