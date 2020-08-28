import numpy

print("*** Triangulate ***")

side1, side2, side3 = int(input("Side 1: ")), int(input("Side 2: ")), int(input("Side 3: "))

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
	if side1 ** 2 + side2 ** 2 == side3 ** 2:
		print("Right-angled triangle")
	if side1 == side2 == side3:
		print("Equilateral triangle")
	elif side1 == side2 or side1 == side3 or side2 == side3:
		print("Isosceles triangle")
	else:
		print("Scalene triangle")
else:
	print("Not a triangle")

side1, side2, angle = int(input("Side 1: ")), int(input("Side 2: ")), int(input("Angle: "))

print(numpy.sqrt(side1 * side1 + side2 * side2 - 2 * side1 * side2 * numpy.cos(numpy.deg2rad(angle))))
