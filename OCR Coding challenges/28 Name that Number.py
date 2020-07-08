print("*** Name that Number ***")

l2n = {
	0: '',
	1: '',
	2: ['A', 'B', 'C'],
	3: ['D', 'E', 'F'],
	4: ['G', 'H', 'I'],
	5: ['J', 'K', 'L'],
	6: ['M', 'N', 'O'],
	7: ['P', 'Q', 'R', 'S'],
	8: ['T', 'U', 'V'],
	9: ['W', 'X', 'Y', 'Z']
}

s = input("Number (xxxx-xxx-xxxx): ")
print(s[:4] + ''.join([''.join([j for j in l2n[int(i)]]) if i != "-" else "-" for i in s]))
