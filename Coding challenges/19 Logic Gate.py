import operator

print("*** Logic Gate ***")

gate = input("Gate: ").lower()

if gate[0] == 'n':
	gate = gate[1:]
	if gate in ['or', 'and']:
		gate = "not operator.%s_" % gate
	else:
		gate = "not operator.%s" % gate
else:
	if gate in ['or', 'and']:
		gate = "operator.%s_" % gate
	else:
		gate = "operator.%s" % gate

print(eval("%s(%d, %d)" % (gate, int(input("Number 1: ")), int(input("Number 2: ")))))

