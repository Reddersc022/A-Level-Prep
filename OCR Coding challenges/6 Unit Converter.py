print("*** Unit Converter ***")

# Converts: 'C -> 'F, m -> ft, and £ -> $

start, val = input("Start value (c, f, m, ft, £, or $): ").lower(), int(input("Value to convert: "))

if start == "'c":
	print((val * 9 / 5) + 32)
elif start == "'f":
	print((val - 32) * 5 / 9)
elif start == 'm':
	print(val * 3.281)
elif start == 'ft':
	print(val / 3.281)
elif start == '£':
	print(val * 1.25)
elif start == '$':
	print(val * .8)
