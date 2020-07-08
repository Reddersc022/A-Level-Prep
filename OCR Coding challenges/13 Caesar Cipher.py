print("*** Caesar Cipher ***")

key, plaintext = int(input("Key: ")), input("Text: ").upper()

if input("Encrypt or Decrypt? (e/d) ") == "e":
	cipherTextList = [ord(i) + key + (6 if 90 < ord(i) + key < 97 else 0) for i in plaintext]
else:
	cipherTextList = [ord(i) - key - (6 if 90 < ord(i) - key < 97 else 0) for i in plaintext]

print(''.join(map(chr, cipherTextList)).upper())
