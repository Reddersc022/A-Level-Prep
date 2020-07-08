print("*** Tiler's Mate ***")

totalArea = int(input("Width: ")) * int(input("Length: "))
cost = int(input("Cost per m^2: "))

print("""
Raw Area   :  %d m^2
Raw Cost   : £%d
-------------------
Final Cost : £%d
""" % (totalArea, totalArea*cost, totalArea*cost*int(input("Labour cost: "))*int(input("Grout cost: "))))
