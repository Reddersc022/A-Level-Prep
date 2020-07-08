print("*** Number Tables ***")

"""
Note: This code can be simplified but I can't be bothered
Also, not doing / to avoid zero division errors
"""

operator, num = input("Operator (+, -, *): "), int(input("Range: ")) + 1

print(operator + " | " + " | ".join([str(i) for i in range(num)]) + " |")
print("---" + "----" * num)

for i in range(num):
    print("%s | %s |" % (i, " | ".join([str(eval("j %s i" % operator)) for j in range(num)])))
