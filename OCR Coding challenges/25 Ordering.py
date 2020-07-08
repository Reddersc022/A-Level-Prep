print("*** Ordering ***")

lst = [sorted(i) for i in input("String: ").split()]
print(''.join([''.join(i) for i in lst]))
