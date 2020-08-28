print("*** Even More Odd ***")

lst = list(input("Items: "))

letters = [i for i in lst if i.isalpha()]
nums = [int(i) for i in lst if i.isnumeric()]
odd = [i for i in nums if i % 2 != 0]
even = [i for i in nums if i % 2 == 0]

print(sorted(letters, reverse=True) + sorted(odd) + sorted(even))
