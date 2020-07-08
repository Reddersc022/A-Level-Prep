print("*** Reverse it ***")


def rev(s: str):
	return s[::-1]


def count(s: str):
	vowels = sum([s.lower().count(i) for i in ['a', 'e', 'i', 'o', 'u']])
	return {"Vowels": vowels, "Consonants": len(s) - vowels}


# For Palindrome, see 20 Palindromes
