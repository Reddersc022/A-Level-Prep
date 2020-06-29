print("*** Palindromes ***")

word = input("Word: ").lower()
print("Palindrome" if word == word[::-1] else "Not a palindrome")
