import math

print("*** Find the Factorial ***")

n = int(input("Number: "))
print(1 if n == 0 else math.prod([i for i in range(1, n+1)]))
