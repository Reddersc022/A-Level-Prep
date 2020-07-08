print("*** FizzBuzz ***")

num, fnum, bnum = int(input("Number: ")), int(input("Fizz num: ")), int(input("Buzz number: "))

print(' | '.join([1 if i == 1
		else "Fizz Buzz" if i % fnum == 0 and i % bnum == 0
		else "Fizz" if i % fnum == 0
		else "Buzz" if i % bnum == 0
		else "Opps" if (i % j == 0 for j in range(i+1))
		else i for i in range(1, num+1)]))  # All in one generator!
