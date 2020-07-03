print("*** Word Subtraction ***")


def sub(a: str, b: str):
	return ''.join([chr(ord(i) - ord(l) + (102 if chr(ord(i) - ord(l)) in ['[', '\\', ']', '^', '_', '`'] else 96))
		for i, l in zip(a, b)])


def subLetters(a: str, b: str):
	for i in a:
		if i in b:
			a.replace(i, "")
			b.replace(i, "")

	return a, b
